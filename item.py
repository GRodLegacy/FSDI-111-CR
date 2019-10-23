class Item:
    id = 0
    title = ""
    cat = ""
    price = 0
    stock = 0

    def __init__(self, id, title, cat, price, stock):
        self.id = id
        self.title = title
        self.category = cat
        self.price = price
        self.stock = stock