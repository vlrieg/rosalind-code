#!/anaconda3/bin/python3

# https://oeis.org/A204631
# solutions: 
# http://saradoesbioinformatics.blogspot.com/2016/06/mortal-fibonacci-rabbits.html
# https://stackoverflow.com/questions/17310051/fibonacci-rabbits-dying-after-arbitrary-of-months
# https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion

from collections import defaultdict

mem = defaultdict(int)

# n = 6 #number of generations
# m = 3 #lifespan in months
# sample data = 4

n = 89 #number of generations
m = 19 #lifespan in months

def seq(x, months):
    if x in mem:
        return mem[x]
    elif x == 0:
        return 1
    elif x == 1:
        return 1
    elif x == 2:
        return 1
    elif x == 3:
        return 2
    else:
        f = seq(x-1, months) + seq(x-2, months) - seq(x-(months+1), months) 
        mem[x] = f
        return f

print(seq(n, m))  