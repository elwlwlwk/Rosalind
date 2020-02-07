from math import factorial
from functools import reduce

with open('rosalind_pper.txt') as f:
    [n, k] = data = f.read().strip().split(' ')
print(reduce(lambda a, b: a*b, list(range(int(n) + 1))[-int(k):]) % 1000000)