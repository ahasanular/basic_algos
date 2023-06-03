def bubble_sort(array: list):
    length = len(array)
    for index in range(length):
        swapped = False
        for j in range(0, length-index-1):
            if array[j] > array[j+1]:
                
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True

        if not swapped:
            break
    return array