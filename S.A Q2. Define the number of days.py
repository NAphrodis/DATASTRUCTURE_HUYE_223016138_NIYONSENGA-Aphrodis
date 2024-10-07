# Define the number of days
num_days = 7
i=0

# Initialize an array to store daily sales
daily_sales = [0] * num_days

# Prompt the user to enter daily sales for each day
for i in range(num_days):
 print(f"Enter the daily sales for day {i+1}:")
 daily_sales[i] = float(input())

# Calculate the average of daily sales
average_sales = sum(daily_sales) / num_days

# Print the average of daily sales
print(f"Average Daily Sales: {average_sales:.2f}")


