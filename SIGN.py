from itertools import permutations, combinations

with open('rosalind_sign.txt') as f:
    n = int(f.read())

numbers = list(range(1, n+1))

all_perms = []
for neg_cnt in range(n+1):
    for neg_nums in combinations(numbers, neg_cnt):
        perm_nums = map(lambda num: str(-num) if num in neg_nums else str(num), numbers)
        all_perms += map(lambda x: ' '.join(x), permutations(perm_nums))

print(len(all_perms))
print('\n'.join(all_perms))
pass