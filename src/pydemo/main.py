# this is main page
from pydemo.index_position.print_position_in_list import *
from pydemo.prime_numbers.prime_list_numbers import *
from pydemo.text_analysis.text_review import *
from pydemo.fibonacci_sequence.fib import *
from pydemo.divisors_of_a_number.divisors import *
from pydemo.sort_integers_list.sort_list import *
#from pydemo.cp_emulation.cp_source_target import *

import pathlib
import sys

file_input = "/Users/bws/BWS/Python/MyFirstProject/src/pydemo/resources/input.txt"
article_name = "/Users/bws/BWS/Python/MyFirstProject/src/pydemo/resources/article.txt"
list_of_numbers = "/Users/bws/BWS/Python/MyFirstProject/src/pydemo/sorted_lists.txt"

if __name__ == '__main__':
    #print(prime_number())
    nr, idx = get_index_number(file_input)
    print(f"Item {nr} has index: {idx}")


    call_text_review_code(article_name)

    # fibonacci sequence
    result_fib = fib_seq(6)
    print("Nth number in the Fibonacci sequence is", result_fib)

    # find the deivisors of a number
    number_div = int(input("Divisors of the number "))
    result_div = divisors(number_div)
    print(result_div)

    # Create two sorted lists
    #number_of_items = int(input("How many items should have the list: "))
    #get_sorted_lists(number_of_items)

    #create a file with two lists on different rows
    #create_list(10)
    print("Concatenated list is:")
    print(get_sorted_lists(list_of_numbers))

    #copy a resorce to a different location
    # ~cp source target
    #copyFile(source, target)




