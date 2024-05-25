class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
        else:
            print("Product ID already exists. Use update_stock method to change quantity.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product ID not found.")

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
            if self.products[product_id].quantity < 0:
                self.products[product_id].quantity = 0
            if self.products[product_id].quantity < 5:
                print("Low stock alert!")
        else:
            print("Product ID not found.")

    def process_sale(self, product_id, quantity):
        if product_id in self.products:
            if self.products[product_id].quantity >= quantity:
                self.products[product_id].quantity -= quantity
                total_cost = self.products[product_id].price * quantity
                print(f"Sale processed. Total cost: RS. {total_cost}")
            else:
                print("Insufficient stock.")
        else:
            print("Product ID not found.")

    def generate_report(self):
        for product_id, product in self.products.items():
            print(f"Product ID: {product_id}, Name: {product.name}, description: {product.description}, quantity: {product.quantity}, Price: RS. {product.price}")

    def generate_low_stock_report(self, threshold=5):
        print("Low Stock Report:")
        for product_id, product in self.products.items():
            if product.quantity < threshold:
                print(f"Product ID: {product_id}, Name: {product.name}, description: {product.description}, quantity: {product.quantity}, Price: RS. {product.price}")
