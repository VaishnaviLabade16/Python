rows = 6

for i in range(rows):
    # spaces before pyramid
    for j in range(rows - i - 1):
        print(" ", end="")

    # pyramid pattern
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()