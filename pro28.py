apr,br=map(int,input().split())
l1=[]
for _ in range(apr):
    l1.append(input())
for i in range(len(l1)):
    if('0' in l1[i]):
        l1[i]=l1[i].replace('0','')
    l1[i]=l1[i].replace(' ','')
lengths=[]
for i in l1:
    if(len(i)>0):
        lengths.append(len(i))
br=min(lengths)
r='1 '*br
r=r.strip()
for i in range(br):
    print(r)
