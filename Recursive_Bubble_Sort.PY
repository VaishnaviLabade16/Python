def recursive_bubble(arr, n):
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    recursive_bubble(arr, n - 1)

arr = [64, 34, 25, 12]
recursive_bubble(arr, len(arr))
print(arr)