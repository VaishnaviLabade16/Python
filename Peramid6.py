rows = 5

for i in range(rows, 0, -1):
    # print spaces
    for j in range(rows - i):
        print(" ", end="")

    # print stars
    for k in range(1, 2*i):
        if i == rows or i == 1 or k == 1 or k == 2*i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()