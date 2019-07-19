api=int(input())
bi=list(map(int,input().split()))
c=0
for m in range(0,api):
	for p in range(0,m):
		if bi[p]<bi[m]:
			c=c+bi[p]
print(c)
