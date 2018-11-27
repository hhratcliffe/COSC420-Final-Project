# this file is used to test and show basic database functionality in terminal
import functions
import time

print("Running driver.py")

# create table
import create_table

# insert items into the table
print("Inserting items into table")
time.sleep(5)
functions.insert("Harry Potter", "J.K. Rowling", "Fiction", "10", "4.1")
functions.insert("Cat in the Hat", "Dr. Seuss", "Fiction", "5", "4.6")
functions.insert("Wocket in my Pocket", "Dr. Seuss", "Fiction", "4", "3.7")

# return a specific item from the table
print("Getting Item from database:")
time.sleep(2)
print(functions.get_item("Harry Potter", "J.K. Rowling"))
print("")

# update an item in the table and return it
print("Updating previous item and returning it:")
time.sleep(2)
functions.update_item("Harry Potter", "J.K. Rowling", "NumInStock", "22")
print(functions.get_item("Harry Potter", "J.K. Rowling"))
print("")

# return items from a certain Author in a table
print("Getting all books by Dr. Seuss:")
time.sleep(2)
functions.query_by_author("Dr. Seuss")
print("")

# return all items in a certain category
print("Gettin all items in 'Fiction' category:")
time.sleep(2)
functions.query_by_category('Fiction')
