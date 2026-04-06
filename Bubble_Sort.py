# Bubble Sort Program

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to check if swapping happens
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping happened, array is already sorted
        if not swapped:
            break

    return arr


# Taking input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Sorting
sorted_numbers = bubble_sort(numbers)

# Output
print("Sorted array:", sorted_numbers)