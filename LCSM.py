from util.read import read_fasta, read_fasta_dict

seqs= list(map(lambda x: x[1], read_fasta('rosalind_lcsm.txt')))
base_seq= seqs[0]
seqs= seqs[1:]
lcs= ''

def check_subseq(subseq, seqs):
	for seq in seqs:
		if subseq not in seq:
			return False
	return True

for i in range(0, len(base_seq)-1):
	for j in range(i+len(lcs), len(base_seq)):
		subseq= base_seq[i:j]
		if check_subseq(subseq, seqs):
			lcs= subseq
print(lcs)
