# DynamoPyLog -- DPL is python log handler which use DynamoDB (by AWS) as storage
# Copyright (C)  2015  Jan Karásek <devel@hkar.eu> http://blog.hkar.eu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import string
import random
import time

import boto.dynamodb2.table


class DynamoHandler(logging.Handler):
    def __init__(self, dynamo_table: boto.dynamodb2.table.Table):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Our custom argument
        self.table = dynamo_table

    @staticmethod
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        """
        Generate pseudo-random id for great namespace distribution in DynamoDB

        :param size:
        :param chars: available chars
        :return: string
        """
        return ''.join(random.choice(chars) for _ in range(size))

    def emit(self, record):
        self.table.put_item(data={
            "id": self.id_generator(),
            "timestamp": time.time(),
            "record": record.message
        })