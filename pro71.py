spa=str(input())
qb=str(input())
s=""
t1=0
t2=0
t=""
r=""
for i in range(0,len(spa)):
    t1=ord(pa[i])-96
    t2=ord(qb[i])+t1
    if(t2>122):
        t2=t2-122
        t2=t2+96
    t=t+chr(t2)
print(t)     
