# Define the number of days
num_days = 7

# Initialize an array to store daily stock prices
daily_stock_prices = [0] * num_days

# Prompt the user to enter daily stock prices for each day
for i in range(num_days):
 print(f"Enter the daily stock price for day {i+1}:")
 daily_stock_prices[i] = float(input())

# Find the maximum and minimum values
max_value = max(daily_stock_prices)
min_value = min(daily_stock_prices)

# Print the maximum and minimum values
print(f"Maximum Daily Stock Price: {max_value:.2f}")
print(f"Minimum Daily Stock Price: {min_value:.2f}")
