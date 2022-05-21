# Find all the divisors of a number

def divisors(n=121):
    divisors_list = []
    # possible divisors
    for i in range(1, n//2 + 1):
        # if rest is 0, add the number as divisor
        if n%i == 0:
            divisors_list.append(i)
    divisors_list.append(n)
    return divisors_list