with open('rosalind_ini.txt') as f:
    data = f.read().strip()

bases = ['A', 'C', 'G', 'T']

count = list(map(lambda base: str(data.count(base)), bases))

print(' '.join(count))