def tournament_sort(arr):
    result = []

    while arr:
        minimum = min(arr)
        result.append(minimum)
        arr.remove(minimum)

    return result

arr = [29, 10, 14, 37, 13]
print(tournament_sort(arr))