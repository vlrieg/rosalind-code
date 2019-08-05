#!/usr/bin/env python3
#http://rosalind.info/problems/ba1e/

import sys
from collections import defaultdict

dna = sys.argv[1]
with open(dna, 'rb') as input_file:
    input = input_file.read().decode('utf-8').splitlines()

genome = input[0].replace(" ", "")
params = input[1].split() #split on whitespace to get out parameters

# store parameters in their own variables
kmers = int(params[0])
length = int(params[1])
times = int(params[2])

def find_clumps(dna, k, l, t):
    matching_seqs = []

    for  clump_start_pos in range(0, (len(dna) - l + 1)):
        clump = dna[clump_start_pos:clump_start_pos+l]
        #print(clump)
        count = defaultdict(int)

        for kmer_index_into_clump in range(0, l-k+1):
            kmer = clump[kmer_index_into_clump:kmer_index_into_clump+k]
            count[kmer] = count[kmer] + 1
        #print(count)
        # for i, j in count.items():
        #     print(i, j)
        for kmer, times in count.items():
            if times >= t:
                matching_seqs.append(kmer)
    return(' '.join(set(matching_seqs)))

x= find_clumps(genome, kmers, length, times)
print(x)