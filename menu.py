import datetime

def get_date_time():
    current = datetime.datetime.now()
    time = current.strftime("%c")
    return time

def print_menu():
    print("\n")
    print('*' * 60)
    print("   Warehouse Inventory System   " + get_date_time())
    print("*" * 60)
    print("\n")

    print("[1] Register new item")
    print("\n")
    print("[2] See all items")
    print("\n")
    print("[3] Update stock")
    print("\n")
    print("[4] Items in stock")
    print("\n")
    print("[5] Remove an item from inventory")
    print("\n")
    print("[6] Register an entry") # the warehouse purchased some stuff
    print("\n")
    print("[7] Register an output") # you sold something
    print("\n")
    print("[8] See log of events")
    print("\n")
    print("[9] See stock value ")
    print("\n")
    print("[x] Exit the system")
    print("\n\n") 