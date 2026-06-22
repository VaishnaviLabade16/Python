def brick_sort(arr):
    n = len(arr)
    sorted_flag = False

    while not sorted_flag:
        sorted_flag = True

        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False

        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False

    return arr

print(brick_sort([34, 2, 10, 6]))