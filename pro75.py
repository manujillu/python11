k1p,n = map(int,input().split())
u2 = list(map(int,input().split()))
v1 = int(input())
w = (sum(u2)-u2[n])//2
if v1==w:
  print("Bon Appetit")
else:
  print(v1-w)
