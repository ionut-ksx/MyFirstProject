# weekend1.py
############## Request 1 ##################
# Print the Nth number in the Fibonacci sequence (google for rule). 0 <= N <=1 000 000
import timeit

""" 1. Fn = Fn-1 + Fn-2, where n > 1."""


def fib_seq(n):
    seq_list = [0, 1]

    # get result
    def get_nth(key):
        return seq_list[key]

    # go through the sequence and calculate its values
    def set_fib_seq(n):
        if n <= 2:
            print(f"Number must be >= 2")
        else:
            for i in range(2, n + 1):
                s = seq_list[i - 1] + seq_list[i - 2]
                seq_list.append(s)
        # call get_nth
        return get_nth(n)
    # call set_fib_seq
    return set_fib_seq(n)