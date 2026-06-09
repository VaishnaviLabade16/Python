def binary_search(arr, item, low, high):
    if high <= low:
        return low + 1 if item > arr[low] else low

    mid = (low + high) // 2

    if item == arr[mid]:
        return mid + 1

    if item > arr[mid]:
        return binary_search(arr, item, mid + 1, high)

    return binary_search(arr, item, low, mid - 1)

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        pos = binary_search(arr, key, 0, j)

        while j >= pos:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

arr = [37, 23, 0, 17, 12, 72, 31]
print(binary_insertion_sort(arr))