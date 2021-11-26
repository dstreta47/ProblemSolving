# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­drome.
#  A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

# Tact Coa
# O(n)
def check_pali_per(string):
    dict1 = {}
    cnt = 0
    for i in range(len(string)):
        if string[i] not in dict1:
            dict1[string[i]] =1
        else:
            dict1[string[i]] += 1    

    for key,val in dict1.items():
        if val !=2:
            cnt+=1
        if cnt >1:
            print("False")      



test = 'tact coa'
test = 'fggkkke'
test = test.replace(" ","")
print(check_pali_per(test))        


