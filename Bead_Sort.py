def bead_sort(arr):
    if any(x < 0 for x in arr):
        return "Only positive integers allowed"

    for _ in range(max(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

arr = [5, 3, 1, 7, 4]
print(bead_sort(arr))