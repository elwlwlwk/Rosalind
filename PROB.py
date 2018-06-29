from functools import reduce
import math
with open('rosalind_prob.txt') as f:
	data= f.read().strip().split('\n')

gc_contents= map(lambda x: float(x), data[1].strip().split(' '))

result= list(map(lambda gc_content: str(math.log10(reduce(lambda a,b: a*b, map(lambda base: gc_content/2 if base in 'GC' else (1-gc_content)/2, data[0])))), gc_contents))
print(' '.join(result))
