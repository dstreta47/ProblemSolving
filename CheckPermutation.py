# Check Permutation: Given two strings,write a method to decide if one is a permutation of the
# other.

def perm_checker_1(test1,test2):
    res1 = sorted(test1)
    res2 = sorted(test2)
    return res1==res2

def perm_checker_2(test1,test2):
    if len(test1)!=len(test2):
        return -1

    char = [0]*256
    for i in range(len(test1)):
        char[ord(test1[i])]+=1
        char[ord(test2[i])]-=1
    print(char)
    for i in char:
        if i <0:
            return True
        else: 
            return False            

test1 = 'abc'
test2 = 'abc'

print(perm_checker_2(test1,test2))
