from util.func_tools import convert_codon
with open('rosalind_prot.txt') as f:
    data = f.read().strip()

protein_string = ''
for idx in range(0, len(data), 3):
    protein_string += convert_codon(data[idx: idx+3])
protein_string = protein_string.replace('Stop', '')

print(protein_string)
