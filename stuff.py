#!/usr/bin/python3
from fractions import Fraction as F
from pprint import pformat as pf
def And(a:F,b:F)->F:
    return a*b
def Or(a:F,b:F)->F:
    return 1-(1-a)*(1-b)
def Not(a:F)->F:
    return 1-a
def OrMany(a:F,n:int)->F:
    return 1-Not(a)**n

pearlChance=F(1,10)

normal_chance=pearlChance**12

chunkInside=F(2,16)
chunkTouching=F(2,16)
chunkOutside=1-chunkInside-chunkTouching

corner11=pearlChance**2
corner12=pearlChance**3
corner22=pearlChance**4
cornerII=Or(Or(corner11,corner22),OrMany(corner12,2))
totalII=And(cornerII,chunkInside**2)
corner31=pearlChance**4
corner32=pearlChance**5
cornerIT=Or(corner31,corner32)
totalIT=And(cornerIT,OrMany(And(chunkInside,chunkTouching),2))
corner33=pearlChance**6
totalTT=And(corner33,chunkTouching**2)
sliceO1=pearlChance**5
sliceO2=pearlChance**7
sliceO3=pearlChance**9
totalOI=And(Or(sliceO1,sliceO2),OrMany(And(chunkInside,chunkOutside),2))
totalOT=And(sliceO3,OrMany(And(chunkInside,chunkTouching),2))
portalOO=pearlChance**12
totalOO=And(portalOO,chunkOutside**2)
total_total=totalII+totalIT+totalTT+totalOI+totalOT+totalOO
just11corner=And(corner11,chunkInside**2)
fraction11=just11corner/total_total

print(pf(locals()))
print("OK.")
for k,v in list(locals().items()):
    if(isinstance(v, F)):
        print(k,'\t=>',f"{float(v):1.15f}",v)


