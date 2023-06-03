def selection_sort(array: list):
    length = len(array)
    for index in range(length):
        min_index = index
        for j in range(index+1, length):
            if array[min_index] > array[j]:
                min_index = j
        
        temp = array[index]
        array[index] = array[min_index]
        array[min_index] = temp

    return array