from functools import reduce

with open('rosalind_tree.txt') as f:
    nodes, *edges = f.read().strip().split('\n')

segments = []

adj_nodes = reduce(lambda a, b: set(a).union(set(b)), map(lambda x: x.split(' '), edges))
for node in range(1, int(nodes) + 1):
    if str(node) not in adj_nodes:
        segments.append(set([str(node)]))

for edge in edges:
    new_cluster = True
    e1, e2 = edge.split(' ')
    for segment in segments:
        if e1 in segment or e2 in segment:
            segment.add(e1)
            segment.add(e2)
            new_cluster = False
    if new_cluster is True:
        segments.append(set([e1, e2]))

def merge_dup(segments):
    new_segments = segments[0:]
    for seg1 in segments:
        for seg2 in segments:
            if seg1 != seg2 and len(seg1.intersection(seg2)) > 0:
                new_seg = seg1.union(seg2)
                new_segments.remove(seg1)
                new_segments.remove(seg2)
                new_segments.append(new_seg)
                return new_segments
    return segments

prev_seg_len = 0
while prev_seg_len != len(segments):
    prev_seg_len = len(segments)
    segments = merge_dup(segments)

print(len(segments) - 1)
pass