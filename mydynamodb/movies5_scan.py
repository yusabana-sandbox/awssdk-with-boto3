from __future__ import print_function
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
import movies_common


dynamodb = boto3.resource('dynamodb')
# dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url='http://localhost:4569')

table = dynamodb.Table('Movies')

print('Movies between 1955 and 1959')

fe = Key('year').between(1955, 1959)
pe = '#yr, title, info.rating'
ean = { '#yr': 'year', }
esk = None

response = table.scan(
    FilterExpression=fe,
    ProjectionExpression=pe,
    ExpressionAttributeNames=ean,
)

# 単純にデフォルトでは20件以上は出ないので最初に20件出して次のwhile分で残りを抽出させる
for i in response['Items']:
    print(json.dumps(i, ensure_ascii=False, cls=movies_common.DecimalEncoder))

while 'LastEvaluatedKey' in response:
    print(json.dumps(i, ensure_ascii=False, cls=movies_common.DecimalEncoder))

    response = table.scan(
        ProjectionExpression=pe,
        FilterExpression=fe,
        ExpressionAttributeNames=ean,
        ExclusiveStartKey=response['LastEvaluatedKey'],
    )

    for i in response['Items']:
        print(json.dumps(i, ensure_ascii=False, cls=movies_common.DecimalEncoder))
