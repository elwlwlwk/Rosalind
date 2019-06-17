from itertools import product

from util.read import read_fasta

seq = read_fasta('rosalind_kmer.txt')[0][1]

bases = ['A', 'T', 'C', 'G']
k = 4
k_mers = map(lambda k_mer: ''.join(k_mer), product(bases, repeat=4))

k_mers_count = dict.fromkeys(k_mers, 0)

for idx in range(len(seq) - k + 1):
    k_mers_count[seq[idx : idx+4]] += 1

print(' '.join(list(map(lambda k_mer: str(k_mers_count[k_mer]), sorted(k_mers_count.keys())))))
pass