#10. Create a 3D array (4 cities x 7 days) to store daily temperature readings for each city
temperature_readings = [
    [[25, 26, 27, 28, 29, 30, 31]],  # City 1 temperatures for 7 days
    [[22, 24, 23, 25, 26, 27, 28]],  # City 2 temperatures for 7 days
    [[30, 29, 28, 27, 26, 25, 24]],  # City 3 temperatures for 7 days
    [[20, 21, 22, 23, 24, 25, 26]]   # City 4 temperatures for 7 days
]

# Manually calculate the total and average temperatures for each city
city_1_total = temperature_readings[0][0][0] + temperature_readings[0][0][1] + temperature_readings[0][0][2] + \
               temperature_readings[0][0][3] + temperature_readings[0][0][4] + temperature_readings[0][0][5] + \
               temperature_readings[0][0][6]
city_1_avg = city_1_total / 7

city_2_total = temperature_readings[1][0][0] + temperature_readings[1][0][1] + temperature_readings[1][0][2] + \
               temperature_readings[1][0][3] + temperature_readings[1][0][4] + temperature_readings[1][0][5] + \
               temperature_readings[1][0][6]
city_2_avg = city_2_total / 7

city_3_total = temperature_readings[2][0][0] + temperature_readings[2][0][1] + temperature_readings[2][0][2] + \
               temperature_readings[2][0][3] + temperature_readings[2][0][4] + temperature_readings[2][0][5] + \
               temperature_readings[2][0][6]
city_3_avg = city_3_total / 7

city_4_total = temperature_readings[3][0][0] + temperature_readings[3][0][1] + temperature_readings[3][0][2] + \
               temperature_readings[3][0][3] + temperature_readings[3][0][4] + temperature_readings[3][0][5] + \
               temperature_readings[3][0][6]
city_4_avg = city_4_total / 7

# Print the average temperature for each city
print("Average Temperature for Each City:")
print("City 1:", city_1_avg)
print("City 2:", city_2_avg)
print("City 3:", city_3_avg)
print("City 4:", city_4_avg)
