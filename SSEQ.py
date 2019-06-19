from util.read import read_fasta

seqs = list(map(lambda row: row[1], read_fasta('rosalind_sseq.txt')))

seq = seqs[0]
sub_seq = seqs[1]

idxs = []

cur_idx = 0
for sub_base in sub_seq:
    while seq[cur_idx] != sub_base:
        cur_idx += 1
    idxs.append(cur_idx + 1)
    cur_idx += 1

print(' '.join(map(lambda idx: str(idx), idxs)))
pass