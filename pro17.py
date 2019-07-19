k1i=int(input())
s=0
for p in range(0,k1i):
  if(pow(2,p)>k1i):
    break
  s=k1i-pow(2,p)
print(s)
