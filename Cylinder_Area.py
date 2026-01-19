import math

# Input radius and height
r = float(input("Enter radius of the cylinder: "))
h = float(input("Enter height of the cylinder: "))

# Calculate total surface area
area = 2 * math.pi * r * (r + h)

# Display result
print("Total Surface Area of the cylinder is:", area)
