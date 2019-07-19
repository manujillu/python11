sp,mm=map(int,input().split())
l=[]
for _ in range(sp):
	l.append(sorted(list(map(int,input().split()))))
for i in range(sp-1):
	for j in range(sp):
		for k in range(sp-i):
			if(l[i][j]>l[i+k][j]):
				l[i][j],l[i+k][j]=l[i+k][j],l[i][j]
for i in l:
	print(*i,sep=' ')       
