# This file is based off the one provided by the AWS tutorial: https://aws.amazon.com/getting-started/projects/create-manage-nonrelational-database-dynamodb/ 

import boto3

client = boto3.client('dynamodb', region_name='us-east-1')

try:
    resp = client.delete_table(
        TableName="Inventory",
    )
    print("Table deleted successfully!")
except Exception as e:
    print("Error deleting table:")
    print(e)
