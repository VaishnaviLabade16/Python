def strand_sort(arr):
    output = []

    while arr:
        sublist = [arr.pop(0)]

        i = 0
        while i < len(arr):
            if arr[i] >= sublist[-1]:
                sublist.append(arr.pop(i))
            else:
                i += 1

        output = merge(output, sublist)

    return output

def merge(a, b):
    result = []

    while a and b:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))

    result += a + b
    return result

print(strand_sort([4, 2, 7, 1, 5]))