# This file is based off the one provided by the AWS tutorial: https://aws.amazon.com/getting-started/projects/create-manage-nonrelational-database-dynamodb/

import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Inventory')

# When making a GetItem call, we specify the Primary Key attributes defined on our table for the desired item.
resp = table.get_item(Key={"Title": "Harry Potter", "Author": "J.K. Rowling"})

print(resp['Item'])
