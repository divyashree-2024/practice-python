A=[3,6,7,-5,-2]
#B = []
#C = {}
#for i, v in enumerate(A):
#    if i == len(A)-1:
#        break
#    product =v*A[i+1]
#    B.append(product)
#    C[product] = (v, A[i+1])
#
#import math
#
#max_val=max(B)
#print(C[max_val])

max_val = -999999
vals = ()
for i, v in enumerate(A):
    if i == len(A)-1:
        break
    product =v*A[i+1]
    if product >= max_val:
        max_val = product
print(max_val)