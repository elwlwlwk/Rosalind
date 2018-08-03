from itertools import permutations
with open('rosalind_perm.txt') as f:
	data= int(f.read().strip())

perms= list(permutations(range(1, data+1)))
print(len(perms))
for perm in perms:
	print(' '.join(map(lambda x: str(x), perm)))
