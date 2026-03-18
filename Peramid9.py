radius = 6

for i in range((2 * radius) + 1):
    for j in range((2 * radius) + 1):
        # Distance formula
        if (i - radius) * 2 + (j - radius) * 2 <= radius ** 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()