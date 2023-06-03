def insertion_sort(array: list):
    for index in range(1, len(array)):
        value = array[index]

        i = index - 1
        while i>=0:
            if value < array[i]:
                array[i+1] = array[i]
                array[i] = value
                i -= 1
            else:
                break

    return array