#!/anaconda3/bin/python3
#http://rosalind.info/problems/subs/

import sys

#read in a file
with open(sys.argv[1], 'r') as data_file:
    data = data_file.read()

data_list = data.split('\n')
sequence = data_list[0]
motif = data_list[1]
#print(f"The sequence is: {sequence} and the motif is: {motif}.")

def motif_finder(string, pattern):
    position = []
    seq_length = len(string)
    motif_length = len(pattern)

    #checks for the motif at each base along the sequence
    #so you will get every instance of the motif, not just the first
    for base in range(seq_length):
        if string[base:base+motif_length] == pattern:
            position.append(base + 1)
    return position

output = ' '.join(map(str, motif_finder(sequence, motif)))
print(output)