def pattern_search(text,pat):
    m = len(pat)-1
    n = len(text)-1

    for i in range(len(text)):
        j=0
        for j in range(len(pat)):
            print(pat[j],text[i+j])
            if (pat[j]!=text[i+j]):
                break
            if (j==m):
                print(i)

text = 'ABCABCD'
pat = 'ABCD'
print(pattern_search(text,pat))
