# Group 2 - Harrison Ratcliffe, Julia Goyco, Stephanie Schoch, Toby Duncan
# Date: 12/6/18
# pythonToDb.py - Contains all methods to access and do operations on database
import paramiko

# Declaring access keys for data base
# old database info (no longer in use - used for testing)
ip_name_old = 'ec2-35-172-134-127.compute-1.amazonaws.com'
key_name_old = 'server_old_key/pd_finalproject_keypair.pem'

# new database info (currently in use)
ip_name_new = 'ec2-54-87-239-153.compute-1.amazonaws.com'
key_name_new = 'server_new_key/pd_finalproject_keypair.pem'

# global variables
item = []
NumInStock = []
output = ""
string = []

# Opening the shell to the database server for interacting with it
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip_name_new, username='ec2-user', key_filename=key_name_new)

# Opening a seperate shell in order to ensure database is activated
ssh_server = paramiko.SSHClient()
ssh_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_server.connect(hostname=ip_name_new, username='ec2-user', key_filename=key_name_new)

# command to make database active
ssh_server.exec_command('java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb')

# Method for returning the items and there respective stock from the database
def getStock():
    # reseting values every time function is called
    item.clear()
    NumInStock.clear()
    string.clear()
    # Calling command to return all table items
    stdin, stdout, stderr = ssh.exec_command('aws dynamodb scan --table-name Stock --endpoint-url http://localhost:8000')
    for line in stdout.read().splitlines():
        string.append(line.decode("utf-8").strip()) # decoding data from bytes to strings
    itemCheck = False # checking if parse has reached an item name
    numCheck = False # checking if parse has reached the number of an item
    # Looping through command line string and cleaning up the input
    # and storing it in an array
    for str in string:
        if(str=="\"Item\": {"):
            itemCheck = True
        elif(str=="\"Num\": {"):
            numCheck = True
        elif itemCheck:
            temp_index = str.index(':')
            itemCheck = False
            #cleaning up input
            #cleaning up extra input
            str = str[temp_index+2:]
            #removing " from input
            str = str.replace("\"", "")
            #adds item to item list
            item.append(str)
        elif numCheck:
            temp_index = str.index(':')
            numCheck = False
            # cleaning up input
            # cleaning up extra input
            str = str[temp_index + 2:]
            # removing " from input
            str = str.replace("\"", "")
            NumInStock.append(str)

# method to return the list of items (books) in database
def getItemList():
    return item

# method to return how many of each book is available
def getNumInStockList():
    return NumInStock

# method for getting new book info and adding a new book plus its stock to the database
def addNewItem(item_name, num_in_stock):
  ssh.exec_command("aws dynamodb put-item --table-name Stock --item \'{\"Item\": {\"S\" : \""+
                                             item_name+"\"}, \"Num\":{\"N\":\""+
                                             num_in_stock+"\"}}\' --endpoint-url http://localhost:8000")

# method for removing a book from the database
def removeItem(item_name):
    ssh.exec_command("aws dynamodb delete-item --table-name Stock --key=\'{\"Item\": {\"S\" : \"" +
                     item_name + "\"}}\' --endpoint-url http://localhost:8000")

# method for updating book and/or stock in database
def updateItem(item_name, num_in_stock_update):
    ssh.exec_command("aws dynamodb update-item --table-name Stock --key=\'{\"Item\": {\"S\" : \"" +
                     item_name + "\"}}\' --update-expression \"SET Num = :c\" --expression-attribute-values "
                                 "\'{ \":c\":{\"N\": \"" + num_in_stock_update+ "\"}}\' "
                                 "--return-values ALL_NEW --endpoint-url http://localhost:8000")