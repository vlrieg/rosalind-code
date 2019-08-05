#!/anaconda3/bin/python3
#http://rosalind.info/problems/ini5/

import sys

with open(sys.argv[1], 'r') as text_file:
    text = text_file.read()

text_lines = text.split('\n')
lines_length = len(text_lines)

for line in range(1, lines_length, 2):
    print(text_lines[line])