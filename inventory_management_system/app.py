from product import Product
from inventory import Inventory

def main():
    # Create instance of the products
    p1 = Product(1, "Shirt", "Blue shirt", 20, 10)
    p2 = Product(2, "Pants", "Black pants", 30, 8)

    # print the created products
    print("Printing the products")
    print(p1)
    print(p2)
    print("\n")


    # Create instance of the inventory
    inventory = Inventory()

    # Add products to inventory
    inventory.add_product(p1)
    inventory.add_product(p2)

    # Generate report after adding the products
    print("Initial Inventory Report:")
    inventory.generate_report()  
    print("\n")

   # Update product info
    p1.update_info(description="Red shirt", price=30)

    # Generate report after updating p1
    print("Inventory Report after updating p1:")
    inventory.generate_report()  
    print("\n")

    # Update stock
    inventory.update_stock(1, -5)

    # Generate report after updating stock of p1
    print("Inventory Report after updating stock:")
    inventory.generate_report()  
    print("\n")

    # Process sale
    print("prossing sales")
    inventory.process_sale(1, 3)
    print("\n")

    # Generate report after processing sale
    print("Inventory Report after processing sale:")
    inventory.generate_report()  
    print("\n")

    # Generating low stock report 
    inventory.generate_low_stock_report()
    print("\n")

    # Remove product
    inventory.remove_product(2)

    # Generate report after removing p2
    print("Inventory Report after removing p2:")
    inventory.generate_report() 
    print("\n")

if __name__ == "__main__":
    main()
