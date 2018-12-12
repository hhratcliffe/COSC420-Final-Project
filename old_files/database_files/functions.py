# This file's functions are based off the files provided by the AWS tutorial: https://aws.amazon.com/getting-started/projects/create-manage-nonrelational-database-dynamodb/

import boto3
from boto3.dynamodb.conditions import Key
import time

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Inventory')

# When making a GetItem call, we specify the Primary Key attributes defined on our table for the desired item.
def get_item(book_title, author):
    return table.get_item(Key = {"Title": book_title, "Author": author})['Item']

# insert a specified item into the table
def insert(book_title, author, category_type, num_in_stock, current_rating):
    with table.batch_writer() as batch:
        batch.put_item(Item={"Title": book_title, "Author": author, "Category": category_type, "NumInStock": num_in_stock, "Rating": current_rating})

# gets all items in a table made by the specified manufacturer
def query_by_author(author):
    resp = table.query(KeyConditionExpression=Key('Author').eq(author))

    print("The query returned the following items:")
    for item in resp['Items']:
        print(item)

# updates the specified field of a certain item
def update_item(book_title, author, update_field, update_value):
    table.update_item(
        Key={"Title": book_title, "Author": author},
        # Expression attribute names specify placeholders for attribute names to use in your update expressions.
        ExpressionAttributeNames={
            "#update": update_field,
        },
        # Expression attribute values specify placeholders for attribute values to use in your update expressions.
        ExpressionAttributeValues={
            ":id": update_value,
        },
        # UpdateExpression declares the updates we want to perform on our item.
        # For more details on update expressions, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html
        UpdateExpression="SET #update = :id",
)


# category is a secondary key added after the table creation
def query_by_category(category):
    # When adding a global secondary index to an existing table, you cannot query the index until it has been backfilled.
    # This portion of the script waits until the index is in the 'ACTIVE' status, indicating it is ready to be queried.
    while True:
        if not table.global_secondary_indexes or table.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE':
            print('Waiting for index to backfill...')
            time.sleep(5)
            table.reload()
        else:
            break

    # When making a Query call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
    # If we want to use a specific index, we also need to pass the IndexName in our API call.
    resp = table.query(
    # Add the name of the index you want to use in your query.
        IndexName="CategoryIndex",
        KeyConditionExpression=Key('Category').eq(category),
    )

    print("The query returned the following items:")
    for item in resp['Items']:
     print(item)
