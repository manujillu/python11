sp=int(input())
ba1=0
le=[]
for sp in range(1,sp+1):
  le.append(sp)
for sp in range(len(le)):
  for sp in range(sp+1,len(le)):
    ba1+=1
print(ba1)
