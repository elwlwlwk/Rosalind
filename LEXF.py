from itertools import permutations

with open('rosalind_lexf') as f:
    data = f.read().strip().split('\n')

symbols = data[0].split(' ')
num = int(data[1])

result = symbols.copy()
for i in range(num - 1):
    cur_result = []
    for symbol in symbols:
        for cur in result:
            cur_result.append(cur+symbol)
    result = cur_result

print('\n'.join(sorted(result)))