def bucket_sort(arr):
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(num * bucket_count)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

print(bucket_sort([0.42, 0.32, 0.23, 0.52, 0.25, 0.47]))