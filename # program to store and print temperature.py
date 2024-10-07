# program to store and print temperature readibg of city for 7 days
num_days = 7
# initialise an array to store temperature reading of acity for 7 days
Temp_readings = [0]*num_days
for i in range(num_days):
    # store temperature reading
    print(f"enter you temperature reading for day {i+1}")
    Temp_readings[i] = float(input())
    # print temperature readings of a city
    print("temperature readings of a city:")
    for i in range(num_days):
     print(f"day {i+1}:{Temp_readings[i]:.2f}")
