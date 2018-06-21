with open('rosalind_hamm.txt') as f:
	data= f.read().strip().split('\n')
print(len(list(filter(lambda x: x[0]!= x[1], zip(*data)))))
