from functools import reduce
import itertools
with open('rosalind_iprb.txt') as f:
	data= f.read().strip().split(' ')
organisms=[]
organisms+=['AA' for i in range(int(data[0]))]
organisms+=['Aa' for i in range(int(data[1]))]
organisms+=['aa' for i in range(int(data[2]))]
all_comb= reduce(lambda a,b: a+b, list(map(lambda x: list(itertools.product(x[0],x[1])), itertools.combinations(organisms,2))))
dominant_num= len(list(filter(lambda x: 'A' in x, all_comb)))
print(dominant_num/len(all_comb))
