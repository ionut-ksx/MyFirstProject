from pydemo.main import *


def test_index_nr():
    number, index = get_index_number(file_input)
    assert str(index) == "9"


def test_fib_nr():
    fib_nr = fib_seq(6)
    assert str(fib_nr) == "8"


def test_divisors_list():
    list_of_divisors = divisors(121)
    assert str(list_of_divisors) == "[1, 11, 121]"


def concatenate_two_lists():
    full_list = get_sorted_lists(list_of_numbers)
    print(full_list)
    assert str(full_list) == "[1, 2, 3, 4, 5, 6, 7, 8]"
