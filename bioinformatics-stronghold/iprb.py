#!/anaconda3/bin/python3
import math

#solution with description of the math required: http://xanhahn.me/rosalind-iprb/


k = 29 #homozygous dominant individuals
m = 19 #heterozygous individuals
n = 25 #homozygous recessive individuals
total = k + m + n #all individuals in the population

d_d = (m / total) * ((m-1)/(total - 1))
d_r = ((m / total) * (n / (total - 1))) + ((n / total) * (m / (total - 1)))
r_r = (n / total) * ((n-1)/(total - 1))

k_total = r_r + (d_d * 1/4) + (d_r * 1/2) #probability of getting recessive genotype
answer = 1 - k_total #1 - k_total gives you the probability of getting dominant genotype

print(answer)