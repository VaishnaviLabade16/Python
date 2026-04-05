rows = 5

for i in range(1, rows + 1):
    # spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # alphabets
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == rows:
            print(chr(64 + i), end="")  # A, B, C...
        else:
            print(" ", end="")
    print()