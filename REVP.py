from util.read import read_fasta

data = read_fasta('rosalind_revp.txt')[0][1]

def get_complement(seq):
    return ''.join(map(lambda base: 'T' if base=='A' else 'A' if base=='T' else 'C' if base=='G' else 'G', seq))

for length in range(4,13,2):
    for idx in range(len(data)-length+1):
        upstream = data[idx:idx+length]
        if get_complement(upstream)[::-1] == upstream:
            print(idx+1, length)