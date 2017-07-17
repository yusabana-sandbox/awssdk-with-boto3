from __future__ import print_function # Helper class to convert a DynamoDB item to JSON.
import boto3
import json
import decimal
import random
import movies_common

dynamodb = boto3.resource('dynamodb')
# dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url='http://localhost:4569')

table = dynamodb.Table('Movies')
title = 'The ほげほげ'
year = 2017
response = table.put_item(
    Item={
        'year': year,
        'title': title,
        'info': {
            'plot': 'Nothing happens at all.',
            'rating': decimal.Decimal(0)
        }
    }
)

print('PutItem succeeded:')
print(json.dumps(response, indent=4, cls=movies_common.DecimalEncoder))
