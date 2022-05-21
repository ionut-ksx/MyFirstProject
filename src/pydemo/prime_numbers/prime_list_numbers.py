# prime_no.py
"""given an integer N, 2 < N < 2 000 000, print (or write to a file) all the prime numbers smaller than it"""
import math


def get_prime_list(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(math.sqrt(num) + 1)):

            # If num is divisible by any number between 2 and n / 2, it is not prime
            if (num % i) == 0:
                # print(num, "is not a prime number")
                break
        else:
            #print(num, "is a prime number")
            return num


def prime_number():
    # iterate the list and print the prime numbers
    num = int(input("Get prime numbers of a number <range 0-2000000>: "))
    prime_list = []
    if num <= 1:
        print(f"{num} is not a prime number")
    else:
        for x in reversed(range(2, num + 1)):
            prime = get_prime_list(x)
            if prime is not None:
                prime_list.append(prime)
    return prime_list
