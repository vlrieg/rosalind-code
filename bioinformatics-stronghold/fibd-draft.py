#!/anaconda3/bin/python3
# http://rosalind.info/problems/fibd/
# in this problem, rabbits are mortal (only live for some # of months)
# assume each pair of rabbits produces 1 pair of rabbit offspring each month (if they are >1 month old)

from collections import defaultdict

n_months = 6 #timeframe
m_lifespan = 3 #lifespan

mem = defaultdict(int)
def mortalrab(months):
    if months in mem:
        return mem[months]
    elif months <= 2:
        return 1
    else:
        f = (mortalrab(months - 1) + (mortalrab(months - 2)))
        mem[months] = f
        return f


#print(mortalrab(n_months, m_lifespan))


# # mortal rabbits -> NO
# n_months = 10 #timeframe
# m_lifespan = 4 ############################## answer needs to be a function of this lifespan!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# rabbit_log = defaultdict(int)

# list_months = [0 for i in range(m_lifespan)] # the list will vary in length by number of months the rabbits are alive
# list_months[0] = 1 #set the number of baby rabbits to 1 (starting conditions)
# #print(list_months)

# for timepoint in range(n_months):
#     if timepoint == 0:
#         rabbit_log[timepoint] = list_months
#     else:
#         previous_values = []
#         for month in range(m_lifespan):
#             count = list(rabbit_log.values())#[timepoint - 1][month]
#             previous_values.append(count)
# print(f"Timepoint: {timepoint} and previous values: {previous_values}")

#only works for m_lifespan = 3
# for timepoint in range(n_months):
#     if timepoint == 0:
#         rabbit_log[timepoint] = [1, 0, 0]
#     else:
#         prev_0 = list(rabbit_log.values())[timepoint - 1][0]
#         prev_1 = list(rabbit_log.values())[timepoint - 1][1]
#         prev_2 = list(rabbit_log.values())[timepoint - 1][2]

#         one_month = prev_1 + prev_2
#         two_month = prev_0
#         three_month = prev_1
#         rabbit_log[timepoint] = [one_month, two_month, three_month]


#print(rabbit_log)


