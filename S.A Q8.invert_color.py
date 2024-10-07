# 8.Create a 2D array that represents an RGB image (3 channels for Red, Green, Blue), and invert the colors.

image = [
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],   # Row 1: Red, Green, Blue pixels
    [[125, 125, 125], [255, 255, 255], [0, 0, 0]], # Row 2: Gray, White, Black pixels
    [[100, 150, 200], [50, 75, 100], [25, 50, 75]] # Row 3: Mixed colors
]

# Print original image
print("Original Image (RGB values):")
for row in image:
    print(row)

# Invert the colors (subtract each value from 255)
for i in range(3):  # Iterate over rows
    for j in range(3):  # Iterate over columns
        for k in range(3):  # Iterate over RGB channels
            image[i][j][k] = 255 - image[i][j][k]

# Print inverted image
print("\nInverted Image (RGB values):")
for row in image:
    print(row)

