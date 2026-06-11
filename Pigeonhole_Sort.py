def pigeonhole_sort(arr):
    minimum = min(arr)
    maximum = max(arr)
    size = maximum - minimum + 1

    holes = [0] * size

    for x in arr:
        holes[x - minimum] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            arr[i] = count + minimum
            i += 1
            holes[count] -= 1

    return arr

arr = [8, 3, 2, 7, 4, 6, 8]
print(pigeonhole_sort(arr))