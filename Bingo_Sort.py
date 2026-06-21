def bingo_sort(arr):
    bingo = min(arr)
    largest = max(arr)
    next_bingo = largest

    while bingo < largest:
        start = 0

        for i in range(len(arr)):
            if arr[i] == bingo:
                arr[i], arr[start] = arr[start], arr[i]
                start += 1
            elif arr[i] < next_bingo:
                next_bingo = arr[i]

        bingo = next_bingo
        next_bingo = largest

    return arr

arr = [5, 3, 8, 3, 2, 5, 1]
print(bingo_sort(arr))