# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string. (Note: If implementing in Java,please use a 
# character array so that you can perform this operation in place.)

# Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"

def space20(test,n):
    cnt = 0
    for i in range(len(test)):
        if test[i]== ' ':
            cnt +=1

    l = cnt*3 + (len(test)-cnt)
    res = [0]*l

    for i in reversed(range(len(test))):
        if test[i] == ' ':
            res[l-1] = 0
            res[l-2] = 2
            res[l-3] = '%'
            l-=3
        else:
            res[l-1] = test[i]
            l-=1
    return res        


test= "Mr John Smith "
n= 13 
print(space20(list(test),n))
# Output: "Mr%20John%20Smith"
