def recursive_selection(arr, start=0):
    if start >= len(arr) - 1:
        return arr

    min_index = start

    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i

    arr[start], arr[min_index] = arr[min_index], arr[start]

    return recursive_selection(arr, start + 1)

arr = [29, 10, 14, 37, 13]
print(recursive_selection(arr))