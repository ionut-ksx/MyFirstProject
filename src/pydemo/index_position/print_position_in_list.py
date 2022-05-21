import random
import pdb


def bubble_sort(arr):
    # sort the list

    swap_happened = True
    comparisons = 0
    while swap_happened:
        comparisons += 1
        swap_happened = False
        for num in range(len(arr)-1):
            comparisons += 1
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]


def search_first_occurrence(line2, x):
    result = ""
    for item, value in enumerate(line2):
        if value == x:
            result = item
            #print(f"Element {int(x)} has first occurrence at index {item}", flush=True)
            return result
            break
        elif x not in line2:
            result = "-1"
    return result


def search_using_binary_alg(ll, low, high, item):
    if low > high:
        return '-1'
    else:
        mid = (low + high)//2
        if ll[mid] == item:
            return mid
        elif ll[mid] > item:
            return search_using_binary_alg(ll, low, mid-1, item)
        else:
            return search_using_binary_alg(ll, mid+1, high, item)


def get_index_number(file_input):
    l2 = []
    with open(file_input, "r") as fp:
        x = fp.readline()[2:-1]
        l2 = fp.readline().split()
        # print(l2)
    # get first occurrence of the item
    index = search_first_occurrence(l2, x)
    return x, index

    # get first occurrence of the item using binary search
    #result_bin = search_using_binary_alg(l2, 0, len(l2) - 1, x)
    #print(result_bin)
