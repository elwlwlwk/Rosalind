from itertools import combinations
from functools import reduce
from math import factorial

with open('rosalind_lia.txt') as f:
    data= list(map(lambda x: int(x), f.read().strip().split(' ')))

def combi(n, r):
    return int(factorial(n) / factorial(r) / factorial(n - r))

AaBb_prob= 0.25
total = 2 ** data[0]
# result = reduce(lambda a, b: a+b, map(lambda x: len(list(combinations(range(total), x))) * AaBb_prob ** x * (1 - AaBb_prob) ** (total - x), range(data[1], total+1)))
result = reduce(lambda a, b: a+b, map(lambda x: combi(total, x) * AaBb_prob ** x * (1 - AaBb_prob) ** (total - x), range(data[1], total+1)))
print(result)