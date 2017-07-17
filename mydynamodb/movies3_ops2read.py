from __future__ import print_function # Helper class to convert a DynamoDB item to JSON.
import boto3
import json
import decimal
import random
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import movies_common


dynamodb = boto3.resource('dynamodb')
# dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url='http://localhost:4569')

table = dynamodb.Table('Movies')
title = 'The ほげほげ'
year = 2017

try:
    response = table.get_item(
        Key={
            'year': year,
            'title': title
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Item']
    print('GetItem succeeded:')
    print(json.dumps(item, indent=4, ensure_ascii=False, cls=movies_common.DecimalEncoder))

