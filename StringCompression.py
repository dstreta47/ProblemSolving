# String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def func(test):
    run=1
    res = []
    for i in range(1,len(test)):
        if test[i] !=test[i-1] or run ==9:
            res.append(run)
            res.append(test[i-1])
            run=0
        run+=1    
    res.append(run)    
    res.append(test[i-1])  
    return res


test = 'aabcccccaaa'
print(func(test))
