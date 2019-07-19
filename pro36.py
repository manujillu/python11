def sub(manu): 
    n = len(manu) 
    sub = [1]*n 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if manu[i] > manu[j] and sub[i]< sub[j] + 1 : 
                sub[i] = sub[j]+1
    maximum = 0
    for i in range(n): 
        maximum = max(maximum , sub[i])  
    return maximum
