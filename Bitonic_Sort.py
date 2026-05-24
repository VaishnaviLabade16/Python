def comp_and_swap(arr, i, j, direction):
    if (direction == 1 and arr[i] > arr[j]) or \
       (direction == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

def bitonic_merge(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            comp_and_swap(arr, i, i + k, direction)

        bitonic_merge(arr, low, k, direction)
        bitonic_merge(arr, low + k, k, direction)

def bitonic_sort(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2

        bitonic_sort(arr, low, k, 1)
        bitonic_sort(arr, low + k, k, 0)

        bitonic_merge(arr, low, cnt, direction)

arr = [3, 7, 4, 8, 6, 2, 1, 5]
bitonic_sort(arr, 0, len(arr), 1)
print(arr)