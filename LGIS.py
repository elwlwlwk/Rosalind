with open('rosalind_lgis.txt') as f:
	data= list(map(lambda x: int(x), f.read().strip().split('\n')[1].split(' ')))

def LIS(seq, comp= lambda a,b: a<b):
	dy_map= [(0, -1) for i in range(len(seq))]
	def seek(sub_seq, cur):
		result=(1, -1)
		for idx in range(len(sub_seq)):
			if comp(sub_seq[idx], cur) and dy_map[idx][0]>=result[0]:
				result= (dy_map[idx][0]+1, idx)
		return result
	for idx in range(len(seq)):
		dy_map[idx]=seek(seq[0:idx], seq[idx])
	last= max(zip(dy_map, data), key= lambda x: x[0][0])
	lis= [last[1]]
	cur_idx= last[0][1]
	while dy_map[cur_idx][0] is not 1:
		lis= [data[cur_idx]]+lis
		cur_idx= dy_map[cur_idx][1]
	lis= [data[cur_idx]]+lis
	return lis	
print(' '.join(map(lambda x: str(x), LIS(data))))
print(' '.join(map(lambda x: str(x), LIS(data, lambda a,b: a>b))))
