nusp=int(input())
lis=list(map(int,input().split()))
half=int(nusp/2)
if sum(lis[:half])//len(lis[:half]) == sum(lis[half:])//len(lis[half:]):
    print("yes")
else:
        print("no")
