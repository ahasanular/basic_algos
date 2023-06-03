def execute_linear_search(array: list, to_find):
    print("searching...")
    
    for index, value in enumerate(array):
        if value == to_find:
            return index
    return -1

def linear_search(array:list, to_find):
    search_result = execute_linear_search(array, to_find)

    if search_result == -1:
        print(f"The number '{to_find}' not found in the array!")
    else:
        print(f"Fond '{to_find}' in index [ {search_result} ].")