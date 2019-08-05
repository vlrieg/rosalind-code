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
    if x not in mem:
        #base case:
        if x < 0:
            mem[x] = 0
        elif x == 0:
            mem[x] = 1
        elif x == 1:
            mem[x] = 1
        elif x == 2:
            mem[x] = 1
        elif x == 3:
            mem[x] = 2
        #recursive case:
        else:
            f = seq(x-1, months) + seq(x-2, months) - seq(x-(months+1), months) 
            mem[x] = f
    
    return mem[x]

print(seq(n, m))  