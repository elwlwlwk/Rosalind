from functools import reduce
with open('rosalind_gc.txt') as f:
	data= f.read().strip().split('>')[1:]
data= list(map(lambda line: line.strip().split('\n'), data))
data= list(map(lambda line: [line[0], reduce(lambda a,b: a+b, line[1:])], data))
gc_data= list(map(lambda line: [line[0], len(list(filter(lambda base: base in ['G','C'], line[1])))/len(line[1])*100], data))
gc_data.sort(key= lambda x: x[1])
print(gc_data[-1][0])
print(gc_data[-1][1])
