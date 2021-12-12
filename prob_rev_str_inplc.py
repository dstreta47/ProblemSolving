# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
#Implementation by recursion

#using list to return 
def rev_str(inp,n,out):
    if n == -1:
        return 
    out.append(inp[n])
    rev_str(inp,n-1,out)
    return out

#in-place
def inplace_rev(inp,l,r):
    if l>=r:
        return 
    inp[l],inp[r] = inp[r],inp[l]
    inplace_rev(inp,l+1,r-1)



inp = ["d","e","e","p","t","i"]
n = len(inp)
out = []
print(rev_str(inp,n-1,out))
l=0
r=len(inp)-1
print(inplace_rev(inp,l,r))
print(inp)


