import json
import boto3

bucket = boto3.resource('s3').Bucket('ebayreports')

def lambda_handler(event, context):
    
    name = event['queryStringParameters']['name']
    objects = []
    
    for o in bucket.objects.filter(Prefix=f'FullData/{name}/'):
        objects.append(o.key)
        
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(objects)
    }
