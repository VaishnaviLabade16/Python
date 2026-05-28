def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def pancake_sort(arr):
    n = len(arr)

    for curr_size in range(n, 1, -1):
        max_index = arr.index(max(arr[:curr_size]))

        if max_index != curr_size - 1:
            flip(arr, max_index)
            flip(arr, curr_size - 1)

    return arr

print(pancake_sort([3, 6, 1, 10, 2]))