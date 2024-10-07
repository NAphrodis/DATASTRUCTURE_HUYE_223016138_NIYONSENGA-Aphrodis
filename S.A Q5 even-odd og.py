# Define the number of random numbers
num_random_numbers = 10

# Initialize variables to store the count of even and odd numbers
count_even = (0) * num_random_numbers
count_odd = (0) * num_random_numbers

# Generate a list of random numbers
for i in range(num_random_numbers):
 print(f"Enter your list numbers for num{i+1}:")
 random_numbers = float(input())
# Count the number of even and odd numbers
 if random_numbers % 2 == 0:
    count_even += 1
 else:  # Otherwise, it's odd
    count_odd += 1
# Print the count of even and odd numbers
print(f"Count of Even Numbers:", count_even)
print(f"Count of Odd Numbers:", count_odd)
