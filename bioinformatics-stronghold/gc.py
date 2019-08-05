#!/anaconda3/bin/python3
#http://rosalind.info/problems/gc/
# This script reads in a fasta text file
# calculates the GC content of each sequence
# returns the sequence ID for the seq with the highest GC content AND
# the GC content of that sequence
# note: Rosalind allows for a default error of 0.001 in all decimal answers 

from collections import defaultdict
import sys


with open(sys.argv[1], 'r') as fasta_file:
    data = fasta_file.read()

data_lines = data.split('\n')


seq_dict = defaultdict(str) #will look like {"ID": "sequence"} after the for loop below
id = '' #>accession-no stored without the ">". Overwritten after each new ">" line

#parse the data file
for line in data_lines:

    if line.startswith(">"):
        id = line[1:]    
    else:
        seq_dict[id] += line



gc_dict = {} #{"ID": <gc content>}

#calculate GC content and add to new dictionary
for seq_id, seq in seq_dict.items():
    gc_count = 0
    for letter in seq:
        if letter == "G" or letter == "C":
            gc_count += 1

    gc_dict[seq_id] =  gc_count / len(seq) * 100


high_score = 0
winner = ''

for new_id, gc in gc_dict.items():
    if gc > high_score:
        high_score = gc
        winner = new_id

print(winner)
print(high_score)