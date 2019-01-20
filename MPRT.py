import requests
import re

with open('rosalind_mprt.txt') as f:
    data= f.read().strip().split('\n')

def find_motif(motif, uniprot_id):
    data = requests.get('http://www.uniprot.org/uniprot/%s.fasta' % uniprot_id).text
    fasta_seq = ''.join(data.split('\n')[1:])
    matches = ' '.join(map(lambda match: str(match.start()+1), re.finditer('(?=%s)' % motif, fasta_seq)))
    return uniprot_id, matches

for uniprot_id in data:
    result = find_motif('N[^P][ST][^P]', uniprot_id)
    if len(result[1]) > 0:
        print(result[0])
        print(result[1])
