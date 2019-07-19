import math
p1,q1=map(int,input().split())
n=[]
v=list(map(int,input().split()))
for i in range(0,q1):
        a,b=map(int,input().split())
        n.append([a,b])
for i in n:
        x=i[0]-1
        y=i[1]-1
        print(math.gcd(v[x],v[y]))
