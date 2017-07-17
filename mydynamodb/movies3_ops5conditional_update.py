from __future__ import print_function # Helper class to convert a DynamoDB item to JSON.
import boto3
from botocore.exceptions import ClientError
import json
import decimal
import movies_common

dynamodb = boto3.resource('dynamodb')
# dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url='http://localhost:4569')

table = dynamodb.Table('Movies')
title = 'The ほげほげ'
year = 2017

# Conditional update (will fail)
print('Attempting conditional update...')

try:
    response = table.update_item(
        Key={
            'year': year,
            'title': title,
        },
        UpdateExpression='remove info.actors[0]',
        ConditionExpression='size(info.actors) > :num',
        ExpressionAttributeValues={
            ':num': 3
        },
        ReturnValues='UPDATED_NEW'
    )
except ClientError as e:
    if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
        print('Occurred error')
        print(e.response['Error']['Message'])
    else:
        raise
else:
    print('UpdateItem succeeded:')
    print(json.dumps(response, indent=4, ensure_ascii=False, cls=movies_common.DecimalEncoder))
