def decreasing(n):
    if n == 0:
        return n
        
    print(n)  
    decreasing(n-1)

    return n

decreasing(3) 
