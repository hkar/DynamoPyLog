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
import logging.handlers
import dynamoHandler
import boto.dynamodb2
import boto.dynamodb2.table

# iniciace připojení (základní typ)
conn = boto.dynamodb2.connect_to_region(
    'eu-west-1',
    aws_access_key_id='ACCESS_KEY',
    aws_secret_access_key='SECRET'
)

dynamo_table = boto.dynamodb2.table.Table("dynamo-log", connection=conn)

logging.basicConfig(filename="app.log", level=logging.WARNING)
logger = logging.getLogger()

ch = dynamoHandler.DynamoHandler(dynamo_table)
ch.setLevel(logging.CRITICAL)

logger.addHandler(ch)

# And finally a test
logger.debug('Test 1')
logger.info('Test 2')
logger.warning('Test 3')
logger.error('Test 4')
logger.critical('Test 5')