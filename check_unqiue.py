# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

#time complexity O(n2), space complexity O(1)
def method1(test): 
    help = 0
    for i in range(len(test)):
        if test[i]==test[i]:
            return False
        else:
            return True    

#time complexity O(n), space complexity O(1)
def method2(test):
    char = [0]*256
    for i in range(len(test)):
        char[ord(test[i])] +=1

    for i in range(len(char)):
        if char[i] > 1:
            print(chr(i),"is repeated")   

test = 'Deeppti'
# print(method1(test))
method2(test)
