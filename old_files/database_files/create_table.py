# This file is based off the one provided by the AWS tutorial: https://aws.amazon.com/getting-started/projects/create-manage-nonrelational-database-dynamodb/

### Notes about our Database tables###
# How many tables do we want?
    # one table for the whole inventory?
# how do we want the database to be set up?

# Creates a database table called Inventory with Primary Key schemas of an Items name and manufacturer

import boto3

# boto3 is the AWS SDK library for Python.
# We can use the low-level client to make API calls to DynamoDB.
client = boto3.client('dynamodb', region_name='us-east-1')

try:
    resp = client.create_table(
        TableName="Inventory",
        # Declare your Primary Keys in the KeySchema argument
        # Composite Primary Key - All items with the same partition key are stored together, in sorted order by sort key value.
        KeySchema=[
            {
                "AttributeName": "Author", # PARTITION KEY - Author Name
                "KeyType": "HASH"
            },
            {
                "AttributeName": "Title", # SORT KEY - Book Title
                "KeyType": "RANGE"
            }
        ],

        # Any attributes used in KeySchema or Indexes must be declared in AttributeDefinitions
        # Defines attributes for the table
        AttributeDefinitions=[
            {
                "AttributeName": "Title", # Title will be a String
                "AttributeType": "S"
            },
            {
                "AttributeName": "Author", # Author will be a string
                "AttributeType": "S"
            }
        ],
        # ProvisionedThroughput controls the amount of data you can read or write to DynamoDB per second.
        # You can control read and write capacity independently.
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    print("Table created successfully!")
except Exception as e:
    print("Error creating table:")
    print(e)
