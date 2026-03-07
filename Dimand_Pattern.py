rows = int(input("Enter number of rows: "))

# Upper part
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
        
    for k in range(1, i + 1):
        print(k, end="")
        
    for k in range(i - 1, 0, -1):
        print(k, end="")
        
    print()

# Lower part
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
        
    for k in range(1, i + 1):
        print(k, end="")
        
    for k in range(i - 1, 0, -1):
        print(k, end="")
        
    print()