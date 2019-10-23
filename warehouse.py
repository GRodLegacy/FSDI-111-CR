

"""
Program: Warehouse control system
Functionality:
 1 - register new items on the systems
    * ID(auto generate this)
    * title
    * category
    * price
    * stock

2 - list all of the items in the system

3 - update qty in stock for a selected item

4 - list items with stock(stock>0)

5 - Remove

6 - Register Entry

7 - Register Output

8 - See event log

9 - See stock value



"""


import sys
from menu import print_menu
from item import Item

import datetime

import os

import pickle

item_list = [] # array to store the data
event_log = [] # array to register the events (input/output)
id_count = 1
items_file = "items.data"
log_file = "log.data"

clear = lambda: os.system('cls')  


def save_items():
    try:
        writer = open(items_file, "wb" ) #write binary information
        pickle.dump(item_list, writer)
        writer.close()
        print("Data saved!!")
    
    except:
        print("**Error: Data could not be saved!")

def save_log():
    try:
        writer = open(log_file, "wb" ) #write binary information
        pickle.dump(event_log, writer)
        writer.close()
        print("Log saved!!")

    except:
        print(" **Error: Log could not be saved!!")

def read_items():
    global id_count
    global items_file

    try:
        reader = open(items_file, "rb")
        temp_data = pickle.load(reader)

        for item_list in temp_data:
            item_list.append(item_list)

        last = item_list[-1]
        id_count = last.id + 1

        print("Items loaded." + str(len(item_list)) + " items")

    except:
        print(" **Error: Item could not be loaded!")

def read_events():
    global log_file

    try:
        reader = open(log_file, "rb")
        temp_data = pickle.load(reader)

        for event in temp_data:
            event_log.append(event)

        print("Events loaded")

    except:
        print(" **Error: Log events could not be loaded!")

def register_entry(action):
    item = select_item()
    if(item is not None):
        how_many = int(input("How many items are you adding/substracting? "))

        if(action == 1):
            item.stock += how_many
            event = str(item.id) + " " + str(how_many) + " input"
            event_log.append(event)
        elif(action == 2):
            item.stock -= how_many
            event = str(item.id) + " " + str(how_many) + " output"
            event_log.append(event)

        save_log()

def remove_item():
    item = select_item()
    if(item is not None):
        try:
            item_list.remove(item)
            print("Item removed!")
        except:
            print("**Error: Item was not removed!")
            print("**Error: ", sys.exc_info()[0])



"""
Stock Value:
- travel the items array
- get the total(value) for each item (stock * price)
- Sum the totals of each item
- Display the result

"""

def print_inventory_value():
    print("*" * 40)
    print(" Inventory Value")
    print("*" * 40)

    total = 0
    for item in item_list:
        val = round(item.price * item.stock, 2)
        total += val

    print(" Total value of the stock is: $" + str(total))
    print("\n")
    print("*" * 40)


def register_item():
    global id_count
    
    try:
        print("*" * 30)
        print(" Register new Item ")
        print("*" * 30)
        id = id_count
        title = input("What is the item? ")
        cat = input("Under what category? ")
        price = float(input("How much will it cost? "))
        stock = int(input("How many are available? "))

        new_item = Item(id, title, cat, price, stock)

        item_list.append(new_item)
        id_count += 1
        print("Item created!")
        print(str(new_item.stock) + " " + new_item.title + " @ $" + str(new_item.price) + " each")

    except: 
        print("\n\n\n")
        print("****Error**** Verify your input and try again!")
        print("** Error: " + sys.exc_info()[0])






# define the register item function
# ask for the info
# create a new object
# store the object on an array
# item = Item(id, title.......)

def print_log():
    print("\n\n\n")
    print("*" * 40)
    print(" Log of events ")
    print("*" * 40)
    for event in event_log:
        print(event)


def list_all():
    print("\n\n\n")
    print("*" * 30)
    print("List of all items")
    print("*" * 30)
    for item in item_list:
        print("ID:" + str(item.id) + "  Name:" + (item.title) + "  $" + str(item.price) + "  QTY:" + str(item.stock))
    
    if(len(item_list) < 1):
        print("-EMPTY DB, Use option 1 to create an item") 
    print("*"*40)


def items_stocked():
    print("*" * 40)
    print("Items in stock")
    print("*" * 40)
    for item in item_list:
        if(item.stock > 0):
            print(str(item.id) + "  Name:" + format_left(20, item.title) + " $" + str(item.price) + "  QTY:" + str(item.stock))
        
        if(len(item_list) < 1):
            print("No items in stock. Use opc 1 to create a new one - ")
        print("*"*40)



def update_stock():
    item = select_item()
    if(item is not None):
        try:
            #ask for new stock value
            new_stock = int(input("Please provide new stock value: "))
            #assign the stock to item
            item.stock = new_stock
            print("Status: Stock value updated")
        except:
            print("Error: Stock should be an integer number, try again!")

def select_item():
    list_all()
    selection = int(input("Id of item: "))
    try:
        #search the item by ID equal to the selection
        for item in item_list:
            if(item.id == selection):
                return item
    except:
        print(" **Error: ID should be a number, try again!")

    #not found
    print(" **Error: ID not found, check and try again")
    return None

def format_left(how_many, text):
    if(len(text) == how_many):
        return None
    
    # cut the text (substring)
    if(len(text) > how_many):
        return text [0:how_many]
    
    while(len(text) < how_many):
        text = text + " "

    return text

# search for the item with ID equal to selection
# return the matching element
# retrun NONE if not found


# First thing is to read previous data
read_items()
read_events()


 # go to the menu
opc = ''
while (opc !='x'):
    clear()
    print_menu()
    opc = input("Select an option: ")
    clear()


    if(opc == "1"):
        register_item()
        save_items()
    elif(opc == "2"):
        list_all()
    elif(opc == "3"):
        update_stock()
        save_items()
    elif(opc == "4"):
        items_stocked()
    elif(opc == "5"):
        remove_item()
        save_items()
    elif(opc == "6"):
        register_entry(1)
        save_items()
    elif(opc == "7"):
        register_entry(2)
        save_items()
    elif(opc == "8"):
        print_log()
    elif(opc == "9"):
        print_inventory_value()
    if(opc != 'x'):
        input("\n\nPress Enter to continue...")


print("Thank you, Byte Byte!")  