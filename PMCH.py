import math
from util.read import read_fasta

data = read_fasta('rosalind_pmch.txt')[0][1]

nA = data.count('A')
nC = data.count('C')

print(math.factorial(nA) * math.factorial(nC))
