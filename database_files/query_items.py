# This file is based off the one provided by the AWS tutorial: https://aws.amazon.com/getting-started/projects/create-manage-nonrelational-database-dynamodb/ 

import boto3
from boto3.dynamodb.conditions import Key

# boto3 is the AWS SDK library for Python.
# The "resources" interface allows for a higher-level abstraction than the low-level client interface.
# For more details, go to http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Inventory')

# When making a Query API call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
# We're using the Key object from the Boto3 library to specify that we want the attribute name ("Author")
# to equal "John Grisham" by using the ".eq()" method.
resp = table.query(KeyConditionExpression=Key('Manufacturer').eq('Samsung'))

print("The query returned the following items:")
for item in resp['Items']:
    print(item)
