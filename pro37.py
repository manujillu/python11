AA11,BB11=map(int,input().split())
CC11=list(map(int,input().split()))
p=list(map(int,input().split()))
q=[]
a=0
for i in range(AA1):
    x=p[i]/CC11[i]
    q.append(x)
while BB11>=0 and len(q)>0:
    mindex=q.index(max(q))
    if BB11>=CC11[mindex]:
        a=a+p[mindex]
        BB11=BB11-CC1[mindex]
    CC11.pop(mindex)
    p.pop(mindex)
    q.pop(mindex)
print(a)
