# Number of rows for the pyramid
rows = 5
num = 1  # Starting number

for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    
    # Print numbers
    for j in range(i):
        print(num, end=" ")
        num += 1
    
    # Move to next line
    print()