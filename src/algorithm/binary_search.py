def execute_binary_search(array: list, to_find, low, high):
    print("searching...")

    while low <= high:
        # print("iteration :")
        mid = low + (high - low) // 2
        # print("mid : ", mid)
 
        if array[mid] == to_find:
            return mid
 
        elif array[mid] < to_find:
            low = mid + 1
 
        else:
            high = mid - 1
 
    return -1


def binary_search(array: list, to_find: int):
    low = 0
    high = len(array)-1

    search_result = execute_binary_search(array, to_find, low, high)

    if search_result == -1:
        print(f"The number '{to_find}' not found in the array!")
    else:
        print(f"Fond '{to_find}' in index [ {search_result} ].")