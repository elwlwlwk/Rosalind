def read_fasta(f_name):
	with open(f_name) as f:
		data= f.read().strip().split('>')[1:]
	return list(map(lambda x: [x[0], ''.join(x[1:])], list(map(lambda fasta: fasta.strip().split('\n'), data))))

def read_fasta_dict(f_name):
	result={}
	data= read_fasta(f_name)
	for fasta in data:
		result[fasta[0]]= fasta[1]
	return result
