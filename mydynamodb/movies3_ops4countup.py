from __future__ import print_function # Helper class to convert a DynamoDB item to JSON.
import boto3
import json
import decimal
import movies_common

dynamodb = boto3.resource('dynamodb')
# dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url='http://localhost:4569')

table = dynamodb.Table('Movies')
title = 'The ほげほげ'
year = 2017
response = table.update_item(
    Key={
        'year': year,
        'title': title,
    },
    UpdateExpression='set info.rating = info.rating + :val',
    ExpressionAttributeValues={
        ':val': decimal.Decimal(1),
    },
    ReturnValues='UPDATED_NEW',
)

print('UpdateItem succeeded:')
print(json.dumps(response, indent=4, ensure_ascii=False, cls=movies_common.DecimalEncoder))
