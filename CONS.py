from collections import Counter
with open('rosalind_cons.txt') as f:
	data= f.read().strip().split('>')[1:]
data= list(map(lambda line: ''.join(line.strip().split('\n')[1:]), data))
profile= list(map(lambda col: Counter(col), zip(*data)))
consensus= list(map(lambda prof: prof.most_common(1)[0][0], profile))
print(''.join(consensus))
print('A: '+' '.join(map(lambda x: str(x['A']), profile)))
print('C: '+' '.join(map(lambda x: str(x['C']), profile)))
print('G: '+' '.join(map(lambda x: str(x['G']), profile)))
print('T: '+' '.join(map(lambda x: str(x['T']), profile)))
