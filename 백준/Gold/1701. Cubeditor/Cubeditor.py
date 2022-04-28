s = input()
def LPS(s):
    ans = 0
    for i in range(len(s)):
        sub = s[i:]
        L = len(sub)
        lps = [0]*L
        Len = 0
        j = 1
        while j<L:
            if sub[j]==sub[Len]:
                Len+=1
                lps[j]=Len
                j+=1
            else:
                if Len!=0:
                    Len = lps[Len-1]
                else:
                    j+=1
        ans = max(ans,max(lps))
    return ans
print(LPS(s))