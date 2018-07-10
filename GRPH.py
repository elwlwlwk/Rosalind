from functools import reduce
with open('rosalind_grph.txt') as f:
	data= f.read().strip().split('>')[1:]
data= list(map(lambda x: [x[0], ''.join(x[1:])], list(map(lambda fasta: fasta.strip().split('\n'), data))))

prefix_dict={}
postfix_dict={}

for fasta in data:
	prefix= fasta[1][0:3]
	postfix= fasta[1][-3:]
	if prefix not in prefix_dict.keys():
		prefix_dict[prefix]= [fasta[0]]
	else:
		prefix_dict[prefix].append(fasta[0])
	if postfix not in postfix_dict.keys():
		postfix_dict[postfix]= [fasta[0]]
	else:
		postfix_dict[postfix].append(fasta[0])

for postfix in postfix_dict.keys():
	for fasta1 in postfix_dict[postfix]:
		if postfix in prefix_dict.keys():
			for fasta2 in prefix_dict[postfix]:
				if fasta1 is not fasta2:
					print(fasta1, fasta2)
