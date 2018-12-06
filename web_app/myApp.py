from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import testjson
import pythonToDb #Python script for interacting with database
app = Flask(__name__)

#Linking the html files to routes on a server
#Starting page of app, used for getting to other pages
@app.route('/')
def main_page():
	return render_template("index.html")

# Admin login for confirming that user is an admin
# Should not need any more code behind it
@app.route('/admin_login.html')
def admin_login():
    return render_template("admin_login.html")

#submitting an order function
@app.route('/submit_order')
def submit_order():
	item = request.args.get('myitem', 0, type=str)
	num = request.args.get('mynum', 0, type=int)
	pythonToDb.updateItem(item, str(num))
	return jsonify(result="")

@app.route('/add_item')
def add_item():
	item = request.args.get('myitem3', 0, type=str)
	num = request.args.get('mynum2', 0, type=int)
	pythonToDb.addNewItem(item, str(num))
	return jsonify(result = "")
#deleting an item function
@app.route('/delete_item')
def delete_item():
	item = request.args.get('myitem',0,type=str)
	pythonToDb.removeItem(item) # call to db to delete item
	return jsonify(result = "")

#updating an item function
@app.route('/update_item')
def update_item():
	item = request.args.get('myitem2', 0, type=str)
	num = request.args.get('mynum',0, type=int)
	pythonToDb.updateItem(item, str(num)) # call to db to update the item's stock
	return jsonify(result = "")
# Get's order information from user
# Send's html doc list of all items and stock
@app.route('/order.html', methods=['GET', 'POST'])
def order_page():
	items = []
	stock = []
	pythonToDb.getStock()
	items = pythonToDb.getItemList()
	stock = pythonToDb.getNumInStockList()
	data = ""
	counter = 0
	for item in items:
		data += item + " Quantity: " + stock[counter] + " "
		counter += 1
	return render_template('order.html',data=data)

# Get's list of all items and stock
# Sends updates to items and stock
# (new items, delete items, etc.)
@app.route('/admin.html', methods=['GET', 'POST'])
def admin_page():
	items = []
	stock = []
	pythonToDb.getStock()
	items = pythonToDb.getItemList()
	stock = pythonToDb.getNumInStockList()
	data = ""
	counter = 0
	for item in items:
		data += item + " Quantity: " + stock[counter] + " "
		counter += 1
	# Call method to return list of items and stock here
	return render_template('admin.html',data=data)
