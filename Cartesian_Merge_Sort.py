def cartesian_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = cartesian_merge_sort(arr[:mid])
    right = cartesian_merge_sort(arr[mid:])

    return sorted(left + right)

print(cartesian_merge_sort([4,7,2,9,1]))