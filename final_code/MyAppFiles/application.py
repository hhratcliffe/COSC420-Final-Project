# Group 2 - Harrison Ratcliffe, Julia Goyco, Stephanie Schoch, Toby Duncan
# Date: 12/6/18
# application.py - Core web app code and running database functions
# and sending data to and from html document
# info for deploying app via elastic beanstalk gotten from:
# https://medium.com/@miloharper/a-beginner-s-guide-to-creating-your-
# first-python-website-using-flask-aws-ec2-elastic-beanstalk-6a82b9be25e0c

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import pythonToDb  # Python script for interacting with database
application = Flask(__name__)

# flask app

# Linking the html files to routes on a server
# Starting page of app, used for getting to other pages
@application.route('/')
def main_page():
	return render_template("index.html")

# Admin login page
# Confirming that user is an admin
@application.route('/admin_login.html')
def admin_login():
    return render_template("admin_login.html")

# submitting an order function (purchasing book)
@application.route('/submit_order')
def submit_order():
	item = request.args.get('myitem', 0, type=str)
	num = request.args.get('mynum', 0, type=int)
	pythonToDb.updateItem(item, str(num))
	return jsonify(result="") # used to satisfy jQuery

# admin functions
# function to add an item to the database (create new book)
@application.route('/add_item')
def add_item():
	item = request.args.get('myitem3', 0, type=str)
	num = request.args.get('mynum2', 0, type=int)
	pythonToDb.addNewItem(item, str(num))
	return jsonify(result = "") # used to satisfy jQuery

# function to delete an item from the database (delete a book)
@application.route('/delete_item')
def delete_item():
	item = request.args.get('myitem',0,type=str)
	pythonToDb.removeItem(item) # call to db to delete item
	return jsonify(result = "") # used to satisfy jQuery

# function to update an item (updating book information and stock)
@application.route('/update_item')
def update_item():
	item = request.args.get('myitem2', 0, type=str)
	num = request.args.get('mynum',0, type=int)
	pythonToDb.updateItem(item, str(num)) # call to db to update the item's stock
	return jsonify(result = "") # used to satisfy jQuery

# order page
# Send's html doc list of all items and stock to present
# to user
@application.route('/order.html', methods=['GET', 'POST'])
def order_page():
	# declaring lists to store database info
	items = []
	stock = []
	pythonToDb.getStock()
	items = pythonToDb.getItemList()
	stock = pythonToDb.getNumInStockList()
	data = ""
	counter = 0
	# cleaning lists into one string to pass to HTML file
	for item in items:
		data += item + " Quantity: " + stock[counter] + " "
		counter += 1
	return render_template('order.html',data=data)

# admin page
# Send's html doc list of all items and stock to present
# to user
@application.route('/admin.html', methods=['GET', 'POST'])
def admin_page():
	# declaring lists to store database info
	items = []
	stock = []
	pythonToDb.getStock()
	items = pythonToDb.getItemList()
	stock = pythonToDb.getNumInStockList()
	data = ""
	counter = 0
	# cleaning lists into one string to pass to HTML file
	for item in items:
		data += item + " Quantity: " + stock[counter] + " "
		counter += 1
	# Call method to return list of items and stock here
	return render_template('admin.html',data=data)

# activates the applications and runs it
if __name__ == "__main__":
	application.run()