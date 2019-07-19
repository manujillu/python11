import sys 
def inCoinspi(coinspi, mo, V): 
    if (V == 0): 
        return 0
    res = sys.maxsize 
    for i in range(0, mo): 
        if (coinspi[i] <= V): 
            sub_res = inCoinspi(coinspi, mo, V-coinspi[i]) 
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1 
    return res
n,V=list(map(int,input().split()))
coinspi = list(map(int,input().split())) 
mo= len(coinspi) 
print(inCoinspi(coinspi, mo, V)) 

