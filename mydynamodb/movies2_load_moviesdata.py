from __future__ import print_function
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb')
# dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url='http://localhost:4569')

table = dynamodb.Table('Movies')
with open('moviedata.json') as json_file:
    # DynamoDBはfloatに対応していない
    # http://qiita.com/dskst/items/10ea3f0d5899d058734e
    movies = json.load(json_file, parse_float=decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print('Adding movie: ', year, title)

        print(info)
        table.put_item(
            Item={
                'year': year,
                'title': title,
                'info': info,
            }
        )
