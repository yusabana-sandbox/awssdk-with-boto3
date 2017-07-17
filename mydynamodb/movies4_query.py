from __future__ import print_function
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
import movies_common


dynamodb = boto3.resource('dynamodb')
# dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url='http://localhost:4569')

table = dynamodb.Table('Movies')

print('Movies at 2017')
response = table.query(KeyConditionExpression=Key('year').eq(2017))
for i in response['Items']:
    print(i['year'], ':', i['title'])



print('Movies at 2016 and titles A-L, with genres and lead actor')
response = table.query(
    ProjectionExpression='#yr, title, info.genres, info.actors[0]',
    ExpressionAttributeNames={ '#yr': 'year' },  # yearは予約語なので変換が必要
    KeyConditionExpression=Key('year').eq(2016) & Key('title').between('A', 'U'),
)
for i in response['Items']:
    print(json.dumps(i, ensure_ascii=False, cls=movies_common.DecimalEncoder))
