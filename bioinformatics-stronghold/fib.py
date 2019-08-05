#!/anaconda3/bin/python3
#This script uses the Fibonnaci sequence to calculate the number of rabbits present after n months
#producing k pairs of rabbits each month



def rabbit(months, k):
    f1 = 1
    f2 = 1
    
    if months == 1: 
        return f1
    elif months == 2:
        return f2
    else:
        return (rabbit(months - 1, k) + (rabbit(months - 2, k) * k))


#print(rabbit(5, 3)) #19
print(rabbit(34, 2)) #5726623061