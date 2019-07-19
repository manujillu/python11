np3=int(input())
list3=list(map(int,input().split()))
choco1=1
count=0
if list3[0]>list3[1]:
    choco1=choco1+1
    count=count+choco1
else:
    count=choco1
for i in range(1,len(list3)):
    if list3[i]>list3[i-1]:
        choco1=choco1+1
        count=count+choco1
    else:
        choco1=1
        count=count+choco1
print(count)
