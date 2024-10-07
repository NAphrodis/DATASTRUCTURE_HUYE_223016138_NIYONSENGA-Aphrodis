#9. Create a list of lists where each sublist contains [product name, price, stock],and filter products that are out of stock.
products = [
    ["printer", 1200, 5],    # Product 1: name, price, stock
    ["charge", 800, 0],      # Product 2: out of stock
    ["headphone", 400, 3],     # Product 3: name, price, stock
    ["microphone", 300, 0],    # Product 4: out of stock
    ["speaker", 50, 10]     # Product 5: name, price, stock
]

# Create a list to store products that are in stock
in_stock_products = []

# Manually filter products that are in stock
in_stock_products.append(products[0])  # printer
if products[1][2] > 0: in_stock_products.append(products[1])  # charge
in_stock_products.append(products[2])  # headphone
if products[3][2] > 0: in_stock_products.append(products[3])  # microphone
in_stock_products.append(products[4])  # speaker

# Print the in-stock products
print("In-Stock Products:")
for products in in_stock_products:
    print(products)
