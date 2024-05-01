statues=[6,2,3,8]
min_val=min(statues)
max_val=max(statues)
#miss_statue=[]
#for i in range(min_val, max_val):
#    if i not in statues:
#        miss_statue.append(i)
#
#print(len(miss_statue))

print(max_val-min_val-len(statues)+1)