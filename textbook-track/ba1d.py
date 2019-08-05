#!/usr/bin/env python3
#http://rosalind.info/problems/ba1d/

import sys

dna = sys.argv[1]

with open(dna, 'rb') as input_file:
    input = input_file.read().decode('utf-8').splitlines()

pattern = input[0]
genome = input[1]

def pattern_find(dna, kmer):
    start_pos = []
    for i in range(0, (len(dna) - len(kmer)+1)):
        if dna[i:i+len(kmer)] == kmer:
            start_pos.append(str(i))
    return(' '.join(start_pos))

print(pattern_find(genome, pattern))