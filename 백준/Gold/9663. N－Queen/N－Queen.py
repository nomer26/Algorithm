n = int(input())
col = [0]*(n+1)
r_c = [0]*(2*n)
l_c = [0]*(2*n)
def sol(cnt):
    if cnt==n+1:return True
    ret = 0
    for i in range(1,n+1):
        if col[i] or r_c[cnt-i+n] or l_c[cnt+i-1]:continue
        col[i] = True
        r_c[cnt-i+n]=True
        l_c[cnt+i-1]=True
        ret+=sol(cnt+1)
        col[i]=False
        r_c[cnt-i+n]=False
        l_c[cnt+i-1]=False
    return ret
print(sol(1))