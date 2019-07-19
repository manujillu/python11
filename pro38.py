array=int(input())
brry=[int(sp) for sp in input().split()]
brry.sort()
sp=0
xv=0
for i in range(len(brry)):
    if brry[i]>=s:
        xv+=1
    sp=sp+brry[i]
print(xv)
