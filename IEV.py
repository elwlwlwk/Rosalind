from util.func_tools import convert_codon
with open('rosalind_iev.txt') as f:
    data = f.read().strip().split(' ')
    data = list(map(lambda count: int(count), data))

expect = 0

expect += data[0] * 2
expect += data[1] * 2
expect += data[2] * 2
expect += data[3] * 0.75 * 2
expect += data[4] * 0.5 * 2
expect += data[5] * 0 * 2

print(expect)
