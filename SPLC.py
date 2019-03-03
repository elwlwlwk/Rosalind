from util.read import read_fasta
from util.func_tools import DNA_CODON_TABLE
from functools import reduce
from textwrap import wrap

fasta = read_fasta('rosalind_splc.txt')

dna_seq = list(map(lambda x: x[1], fasta))
exon = reduce(lambda a,b: a[0:a.find(b)]+a[a.find(b)+len(b):], dna_seq)
print(''.join(map(lambda codon: DNA_CODON_TABLE[codon], wrap(exon, 3))))

pass