# This file is based off the one provided by the AWS tutorial: https://aws.amazon.com/getting-started/projects/create-manage-nonrelational-database-dynamodb/

import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Inventory')

# We'll use the GetItem API to show what the book looks like before we update it.
resp = table.get_item(Key={"Title": "The Lorax", "Author": "Dr. Seuss"})

print("Item before update:")
print(resp['Item'])

# The UpdateItem API allows us to update a particular item as identified by its key.
resp = table.update_item(
    Key={"Title": "The Lorax", "Author": "Dr. Seuss"},
    # Expression attribute names specify placeholders for attribute names to use in your update expressions.
    ExpressionAttributeNames={
        "#numinstock": "NumInStock",
    },
    # Expression attribute values specify placeholders for attribute values to use in your update expressions.
    ExpressionAttributeValues={
        ":id": "20",
    },
    # UpdateExpression declares the updates we want to perform on our item.
    # For more details on update expressions, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html
    UpdateExpression="SET #numinstock = :id",
)


# Now use the GetItem API to show what the book looks like after the update.
resp = table.get_item(Key={"Title": "The Lorax", "Author": "Dr. Seuss"})

print("Item after update:")
print(resp['Item'])
