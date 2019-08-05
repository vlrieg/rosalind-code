#!/anaconda3/bin/python3
# http://rosalind.info/problems/cons/
# run this script: ./cons.py <file.fasta>

import sys
from collections import defaultdict

#open fasta file
with open(sys.argv[1], 'r') as fasta_file:
    data = fasta_file.read()
data_lines = data.split('\n')

seq_dict = defaultdict(str) #will look like {"ID": "sequence"} after the for loop below
id = '' #>accession-no stored without the ">". Overwritten after each new ">" line

#parse data file
for line in data_lines:

    if line.startswith(">"):
        id = line[1:]    
    else:
        seq_dict[id] += line #+= in case the sequence is across multiple new lines
#print(list(seq_dict.values())[0]) #this is how you access a single value
#print(len(list(seq_dict.values())[0])) #this is how you get the length of the first value
#print(list(seq_dict.values())[0][0]) #this is how you access a single value column


def get_matrix(seqs): #seqs is a list of sequences from the values field of the fasta dictionary created above
    number_of_seqs = len(seqs)
    seq_length = len(seqs[0])

    a_count = []
    c_count = []
    g_count = []
    t_count = []


    #for each column of the sequence
    for num in range(seq_length):

        column_a = 0
        column_c = 0
        column_g = 0
        column_t = 0

        #for each sequence in the dictionary
        for item in range(number_of_seqs):

            column_val = seqs[item][num]
  
            if column_val == 'A':
                column_a += 1 
            elif column_val == 'C':
                column_c += 1
            elif column_val == 'G':
                column_g += 1
            elif column_val == "T":
                column_t += 1
            else:
                print("Not a sequence column?")
        
        a_count.append(column_a)
        c_count.append(column_c)
        g_count.append(column_g)
        t_count.append(column_t)

    freq_matrix = [a_count, c_count, g_count, t_count]
    return freq_matrix


def consensus(val_matrix):
    no_letters = len(val_matrix)
    no_columns = len(val_matrix[0])

    consensus_list = []

    #iterate over column number
    for col in range(no_columns):
        
        column_dict = {'A': int, 'C': int, 'G': int, 'T': int}

        #iterate over each letter
        for num in range(no_letters):

            if num == 0:
                column_dict['A'] = val_matrix[num][col]
            elif num == 1:
                column_dict['C'] = val_matrix[num][col]
            elif num == 2:
                column_dict['G'] = val_matrix[num][col]
            elif num == 3:
                column_dict['T'] = val_matrix[num][col]
            else:
                print("Some kind of error in matrix interpretation?")
        
        highscore = 0
        winner = ''

        for letter, score in column_dict.items():
            if score > highscore:
                highscore = score
                winner = letter

        consensus_list.append(winner)
        
    return ''.join(consensus_list)



# Call the functions
table = get_matrix(list(seq_dict.values()))
output = consensus(table)

# Print the output
print(output) # the consensus sequence

# matrix
print('A: ', end = '') 
for i in range(len(table[0])):
    value = table[0][i]
    print(f'{value} ', end = '')
print()

print('C: ', end = '') 
for i in range(len(table[1])):
    value = table[1][i]
    print(f'{value} ', end = '')
print()

print('G: ', end = '') 
for i in range(len(table[2])):
    value = table[2][i]
    print(f'{value} ', end = '')
print()

print('T: ', end = '') 
for i in range(len(table[3])):
    value = table[3][i]
    print(f'{value} ', end = '')
print()