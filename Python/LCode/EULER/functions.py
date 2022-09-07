import enum
from time import process_time_ns


def primes(n):
    '''
        Implementing Sieve of Eratosthenes
    '''
    p = [True] * n
    p[0] = p[1] = False
    count = 2
    while count <= int(n ** 0.5):
        if p[count]:
            for i in range(count*2, n, count):
                p[i] = False
        count += 1
    return p


def factor_list(n):
    '''
        List of factors for the first n natural numbers
    '''
    factors = [set([1]) for _ in range(n)]
    factors[0] = {0}
    num = 2
    while num < n:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                factors[num].update({i, int(num/i)})
        if (num ** 0.5).is_integer():
            factors[num].update({int(num ** 0.5)})
        num += 1
    return factors


def twosum(arr, target):
    lookup = {}
    for pos, number in enumerate(arr):
        if target - number in lookup:
            return True
        else:
            lookup[number] = pos
    return False
