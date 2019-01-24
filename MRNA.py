from functools import reduce
from util.func_tools import RNA_CODON_TABLE

protein_count = {}

for protein in RNA_CODON_TABLE.values():
    if protein not in protein_count.keys():
        protein_count[protein] = 0
    protein_count[protein] += 1

with open('rosalind_mrna.txt') as f:
    data= f.read().strip()

combi = reduce(lambda a,b: a * b, map(lambda protein: protein_count[protein], data)) * protein_count['Stop']
print(combi % 1000000)