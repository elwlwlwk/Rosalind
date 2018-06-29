from functools import reduce
with open('rosalind_fibd.txt') as f:
	data= f.read().strip().split(' ')

rabbits= [0 for i in range(int(data[1]))]
rabbits[0]= 1

for i in range(int(data[0])-1):
	baby= reduce(lambda a,b: a+b, rabbits[1:])
	rabbits[1:]= rabbits[0:-1]
	rabbits[0]= baby

print(reduce(lambda a,b: a+b, rabbits))
