# lambda_function.py

import json

def lambda_handler(event, context):
    # Example code to handle incoming API request
    if event.get("httpMethod") == "POST":
        response = {
            'statusCode': 200,
            'body': json.dumps('Hello from POST method!')
        }
    else:
        response = {
            'statusCode': 400,
            'body': json.dumps('Unsupported method. Use POST.')
        }
    return response
