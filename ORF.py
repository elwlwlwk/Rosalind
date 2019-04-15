from util.read import read_fasta
from textwrap import wrap
import re
from util.func_tools import DNA_CODON_TABLE

seq = read_fasta('rosalind_orf.txt')[0][1]
complement = ''.join(list(map(lambda base: 'A' if base is 'T' else 'T' if base is 'A' else 'C' if base is 'G' else 'G', seq))[::-1])

result = set()
for idx in range(len(seq)):
    try:
        orf = re.search('ATG(...)*?(?=TAA|TAG|TGA)', seq[idx:]).group()
        result.add(''.join(map(lambda triplet: DNA_CODON_TABLE[triplet], wrap(orf, 3))))
    except:
        pass
    try:
        orf = re.search('ATG(...)*?(?=TAA|TAG|TGA)', complement[idx:]).group()
        result.add(''.join(map(lambda triplet: DNA_CODON_TABLE[triplet], wrap(orf, 3))))
    except:
        pass
print('\n'.join(result))