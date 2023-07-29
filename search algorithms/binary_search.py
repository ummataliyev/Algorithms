def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


myList = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]
search_value = 45
result_index = binary_search(myList, search_value)

if result_index is not None:
    print(f"The value {search_value} is found at index {result_index}.")
else:
    print(f"The value {search_value} is not found in the array.")
