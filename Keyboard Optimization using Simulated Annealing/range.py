import random
import copy

di={1:2,3:4,5:6}
lj=[]
lj.append(copy.deepcopy(di))
di[3]=50000
lj.append(di)
print(lj)

print(random.random())