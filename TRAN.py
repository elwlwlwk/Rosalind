import math
from util.read import read_fasta

data = read_fasta('rosalind_tran.txt')
seq1 = data[0][1]
seq2 = data[1][1]

bases = {
    'A': 'purine',
    'G': 'purine',
    'C': 'pyrimidine',
    'T': 'pyrimidine',
}

transversions = 0
transitions = 0

for (base1, base2) in zip(seq1, seq2):
    if base1 == base2:
        continue
    elif bases[base1] != bases[base2]:
        transversions += 1
    else:
        transitions += 1

print(transitions / transversions)