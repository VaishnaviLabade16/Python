def circle_sort(arr):
    def sort_rec(low, high):
        if low == high:
            return 0

        swaps = 0
        l, r = low, high

        while l < r:
            if arr[l] > arr[r]:
                arr[l], arr[r] = arr[r], arr[l]
                swaps += 1
            l += 1
            r -= 1

        mid = (high - low) // 2

        swaps += sort_rec(low, low + mid)
        swaps += sort_rec(low + mid + 1, high)

        return swaps

    while sort_rec(0, len(arr)-1):
        pass

    return arr

arr = [9, 4, 1, 6, 7]
print(circle_sort(arr))