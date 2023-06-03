from algorithm.insertion_sort import insertion_sort
from algorithm.bubble_sort import bubble_sort
from algorithm.selection_sort import selection_sort
from algorithm.merge_sort import merge_sort
from algorithm.binary_search import binary_search
from algorithm.linear_search import linear_search
import random

def main():
    # array = [1, 5, 6, 80, 21, 64, 0, 80, 3]
    array = [38, 27, 43, 3, 9, 82, 10]
    random_array = []
    
    # for i in range(10):
    #     random_array.append(random.randint(10, 1000))
    # array = random_array

    print(end="\n")
    print("Before : ", array)
    # sorted_array = insertion_sort(array)
    # sorted_array = bubble_sort(array)
    # sorted_array = selection_sort(array)
    merge_sort(array)
    sorted_array = array
    print("After  : ", array, end="\n\n")

    to_find = random.choice(array)
    # to_find = 100
    binary_search(sorted_array, to_find)
    # linear_search(sorted_array, to_find)



if __name__=="__main__":
    main()