#!/usr/bin/env python3
#http://rosalind.info/problems/ba1c/

import sys

dna = sys.argv[1]

with open(dna, 'rb') as input_file:
    sequence = str(input_file.read().decode('utf-8'))

def revc(seq):
    newSeq = []

    for x in seq:
        if x == "T":
            newSeq.append("A")
        elif x == "A":
            newSeq.append("T")
        elif x == "C":
            newSeq.append("G")
        elif x == "G":
            newSeq.append("C")

    newSeq.reverse()
    return(''.join(newSeq))
        

revcompSeq = revc(sequence)
print(revcompSeq)
