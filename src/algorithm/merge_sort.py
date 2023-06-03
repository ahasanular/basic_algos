def merge_sort(array: list):
    if len(array) > 1:
        mid = len(array)//2

        left_ara = array[:mid]
        right_ara = array[mid:]

        # print(left_ara, " ||| ", right_ara)

        print(left_ara, " | ",right_ara)
        
        merge_sort(left_ara)
        merge_sort(right_ara)

        print("merging ... ")
        
        print(left_ara, " | ",right_ara)
        
        i = j = k = 0
        while i < len(left_ara) and j < len(right_ara):
            if left_ara[i] <= right_ara[j]:
                array[k] = left_ara[i]
                i += 1
            else:
                array[k] = right_ara[j]
                j += 1
            k += 1

        while i < len(left_ara):
            array[k] = left_ara[i]
            i += 1
            k += 1
        while j < len(right_ara):
            array[k] = right_ara[j]
            j += 1
            k += 1
            
    
        print("main >> ", array)

