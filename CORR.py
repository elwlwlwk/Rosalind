from util.read import read_fasta
from util.func_tools import get_complement

seqs = list(map(lambda row: row[1], read_fasta('rosalind_corr.txt')))
seqs_with_complements = seqs + list(map(lambda seq: get_complement(seq), seqs))
err_seqs = list(filter(lambda seq: seqs_with_complements.count(seq) == 1, seqs))
correct_seqs = list(filter(lambda seq: seqs_with_complements.count(seq) > 1, seqs_with_complements))
corrected_seqs = list(map(lambda err_seq: list(filter(lambda seq: list(map(lambda base_match: base_match[0] == base_match[1], zip(err_seq, seq))).count(False) == 1, correct_seqs))[0], err_seqs))
print('\n'.join(map(lambda correction: '->'.join(correction), zip(err_seqs, corrected_seqs))))
pass