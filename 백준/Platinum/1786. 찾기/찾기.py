import sys;input =sys.stdin.readline
def KMP(pat,txt):
    cnt = 0
    idx = []
    n = len(txt)
    L = len(pat)
    lps = [0]*L
    LPS(pat,L,lps)
    i,j = 0,0
    while i<n:
        if txt[i]==pat[j]:
            i+=1
            j+=1
            if j==L:
                cnt+=1
                idx.append(i-j+1)
                j = lps[j-1]
        elif i<n and txt[i]!=pat[j]:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1
    return cnt,idx
def LPS(pat,L,lps):
    Len = 0
    i = 1
    while i<L:
        if pat[i]==pat[Len]:
            Len+=1
            lps[i] = Len
            i+=1
        else:
            if Len!=0:
                Len = lps[Len-1]
            else:
                i+=1
    
txt = input().rstrip()
pat = input().rstrip()
cnt,idx = KMP(pat,txt)
print(cnt)
print(*idx)