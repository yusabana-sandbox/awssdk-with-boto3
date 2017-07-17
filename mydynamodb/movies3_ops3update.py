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
    UpdateExpression='set info.rating = :r, info.plot=:p, info.actors=:a',
    ExpressionAttributeValues={
        ':r': decimal.Decimal(5.5),
        ':p': 'Everything happens all at onece.',
        ':a': ['Larry', 'Moe', 'Curry', 'たかえす'],
    },
    ReturnValues='UPDATED_NEW',
)

print('UpdateItem succeeded:')
print(json.dumps(response, indent=4, ensure_ascii=False, cls=movies_common.DecimalEncoder))
