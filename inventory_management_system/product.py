class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def update_info(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Price: RS. {self.price}, Quantity: {self.quantity}"
