import json
import requests

print('Loading function')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    r = requests.get('http://google.com')
    print(r.text[:100])

    # print("val1 = " + event['key1'])
    # print("val2 = " + event['key2'])
    # print("val3 = " + event['key3'])
    # print('aaa: ', event['aaa'])
    # print(event)

    # return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
    return 'Hello WorldAAAAAAAAA!!!!'
