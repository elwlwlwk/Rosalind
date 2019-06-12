from util.read import read_fasta

def weld_seq(seq1, seq2):
    for weld_len in reversed(range(min(len(seq1), len(seq2)))):
        if seq1[-weld_len:] == seq2[0: weld_len]:
            return seq1 + seq2[weld_len:]
    return seq1 + seq2

seqs = list(map(lambda fasta: fasta[1], read_fasta('rosalind_long.txt')))

while len(seqs) > 1:
    weld_result = []
    for seq1 in seqs:
        for seq2 in seqs:
            if seq1 == seq2:
                continue
            welded_seq = weld_seq(seq1, seq2)
            score = abs(len(seq1) + len(seq2) - len(welded_seq))
            weld_result.append([seq1, seq2, welded_seq, score])
    max_weld = max(weld_result, key = lambda x: x[3])
    seqs.remove(max_weld[0])
    seqs.remove(max_weld[1])
    seqs.append(max_weld[2])
print(seqs[0])
pass