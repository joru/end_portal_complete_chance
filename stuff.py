#!/usr/bin/python3
from fractions import Fraction as F
import decimal
D=decimal.Decimal
from pprint import pformat as pf
def And(a:F,b:F)->F:
    return a*b
def Or(a:F,b:F)->F:
    return 1-(1-a)*(1-b)
def Not(a:F)->F:
    return 1-a
def OrMany(a:F,n:int)->F:
    return Not(Not(a)**n)

pearlChance=F(1,10)

assumed_chance=pearlChance**12

chunkInside=F(2,16)
chunkOutside=1-chunkInside

in4chunks=chunkInside**2
in1chunk=chunkOutside**2
in2chunks=1-in1chunk-in4chunks

complete1=in1chunk*assumed_chance
complete2=in2chunks*OrMany(assumed_chance,2)
complete4=in4chunks*OrMany(assumed_chance,4)

complete=complete1+complete2+complete4

difference=complete/assumed_chance


decimal.getcontext().prec=9999
for k,v in list(locals().items()):
    if(isinstance(v, F)):
        print(k,'\t=>',(D(v.numerator)/v.denominator),v)


