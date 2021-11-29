def increasing(n):
    if n == 0:
        return n


    increasing(n-1)  
    print(n) 
    return n

increasing(3) 
