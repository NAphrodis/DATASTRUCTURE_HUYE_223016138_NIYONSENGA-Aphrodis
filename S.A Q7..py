#7.	Store and display the weekly sales of different products in a shop in a 2D array (products x days).
# Create a 2D array representing the sales of different products for each day of the week
sales = [
    [100, 150, 200, 250, 300, 350, 400],  # Product 1 sales (Mon-Sun)
    [120, 130, 180, 210, 260, 290, 310],  # Product 2 sales (Mon-Sun)
    [90,  110, 140, 170, 230, 260, 280],  # Product 3 sales (Mon-Sun)
    [80,  100, 130, 160, 200, 220, 240]   # Product 4 sales (Mon-Sun)
]

# Days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Display sales data
print("Weekly Sales Data:")
print("Product |", " | ".join(days), "|")
print("-" * 60)

# Display sales for each product
for i in range(len(sales)):
    print(f"Product {i+1} |", " | ".join(str(sales[i][j]) for j in range(7)),"|")