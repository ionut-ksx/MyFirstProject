############## Request 3 ##################
# Given a file with 2 sorted lists of integers (each list on its row),
# print a single list with all of the elements from the input lists,
# such that the single list is also sorted.
# Hint: you should not use any sort function here,
# but rely on the property of the inputs.


def get_sorted_lists(list_of_numbers):
    data = []
    # create a list with all elements from line1 and line 2
    with open(list_of_numbers, "r") as f_content:
        for line in f_content:
            for char in line.split():
                char = char.strip(',][')
                if char.isdigit():
                    data.append(char)
    data.sort(key=int)
    return data



def create_list(list_size):
     # I want both lists with the same number of elements
    if list_size%2 == 1:
        list_size += 1

    with open(list_of_numbers, "w+") as sl:
        odd_list = []
        even_list = []
        for num in range(1, list_size+1):
            if num % 2 == 1:
                odd_list.append(num)
            else:
                even_list.append(num)
        sl.writelines(str(odd_list)+"\n")
        sl.writelines(str(even_list))

