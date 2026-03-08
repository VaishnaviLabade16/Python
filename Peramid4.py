# Number of rows in the pyramid
rows = 5
num = 1  # Start number

for i in range(1, rows + 1):
    # Print spaces for alignment
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print numbers in the row
    for k in range(1, i + 1):
        print(num, end=" ")
        num += 1
    
    # Move to next line
    print()