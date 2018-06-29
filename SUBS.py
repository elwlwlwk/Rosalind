import re
with open('rosalind_subs.txt') as f:
	data= f.read().strip().split('\n')
pattern= re.compile('(?=(%s))' % data[1])
result= [str(m.start(0)+1) for m in re.finditer(pattern, data[0])]
print(' '.join(result))
