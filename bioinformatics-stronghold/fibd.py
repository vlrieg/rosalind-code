#!/anaconda3/bin/python3
# http://rosalind.info/problems/fibd/

# sequence for m = 5: https://oeis.org/A204631
# solution: http://saradoesbioinformatics.blogspot.com/2016/06/mortal-fibonacci-rabbits.html


#problems encountered in solving this question:
# 1) figuring out the recursive algorithm (see solution link above)
# 2) without specifying for x<0, you will get an infinite loop
# 3) seq(x<0) should = 0, not 1

from collections import defaultdict

mem = defaultdict(int)

# n = 6 #number of generations
# m = 3 #lifespan in months
# sample data output = 4

n = 88
m = 19

def seq(x, months):
    #base case:
    if x < 0:
        return 0
    elif x == 0:
        return 1
    elif x == 1:
        return 1
    elif x == 2:
        return 1
    elif x == 3:
        return 2
    #recursive case:
    else:
        return seq_memo(x-1, months) + seq_memo(x-2, months) - seq_memo(x-(months+1), months) 

def seq_memo(x, months):
    if x not in mem:
        mem[x] = seq(x, months)    
    return mem[x]

print(seq(n, m))  