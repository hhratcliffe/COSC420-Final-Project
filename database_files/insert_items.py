# This file is based off the one provided by the AWS tutorial: https://aws.amazon.com/getting-started/projects/create-manage-nonrelational-database-dynamodb/ 

# Inserts specified items into a specific database table
# Allows us to insert a large amount of items into the table at once
import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Inventory')

# item structure for insertion is batch.put_item(Item={"Item": "Name of Item", "Manufacturer": "Name of Manufacturer",
# "Category": "Type of Item", "NumInStock": "4", "Rating": "5.0"})

# The BatchWriteItem API allows us to write multiple items to a table in one request.
with table.batch_writer() as batch:
    # Book Below left in temporarily for reference
    #batch.put_item(Item={"Author": "John Grisham", "Title": "The Rainmaker",
     #   "Category": "Suspense", "Formats": { "Hardcover": "J4SUKVGU", "Paperback": "D7YF4FCX" } })

    # Our items start here
    batch.put_item(Item={"Item": "Samsung Galaxy S7", "Manufacturer": "Samsung", "Category": "Electronics", "NumInStock": "3", "Rating": "4.2"})
    batch.put_item(Item={"Item": "Samsung Galaxy S5", "Manufacturer": "Samsung", "Category": "Electronics", "NumInStock": "7", "Rating": "3.2"})
   # batch.put_item(Item={"Item": "Name of Item", "Manufacturer": "Name of Manufacturer", "Category": "Type of Item", "NumInStock": "4", "Rating": "5.0"})
