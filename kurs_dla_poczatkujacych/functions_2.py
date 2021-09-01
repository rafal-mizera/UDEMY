import math

def GiveGeomSeqElement(a1=2,factor=2,index=2):
    #returns n-th term of geometric sequence starting with element a1 and having
    value = a1*pow(factor,index-1)
    return value

a1=3
factor=2
maxindex=10
for i in range(1,maxindex):
    an = GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)

