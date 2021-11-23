def subsequence(string1,string2,n,m):
    if (m==0):
        return True
    if (n==0):
        return False
    print(string1[n-1],string2[m-1])
    if(string1[n-1]==string2[m-1]):
        return  subsequence(string1,string2,n-1,m-1)  
    else:
        return   subsequence(string1,string2,n-1,m)       


print(subsequence('ABCDEF','AfDE',6,4))              
