N,K = map(int,input().split())

def f(n):
    if n==0: return 1
    for i in range(n-1,1,-1):
        n = (n*i)%mod
    return n
def q_p(x,n):
    if n==0:return 1
    if n%2: return (q_p(x,n//2)**2*x)%mod
    return (q_p(x,n//2)**2)%mod
mod = 1_000_000_007
a = f(N)
b = q_p(f(N-K),mod-2)
c = q_p(f(K),mod-2)
print(a*b*c%mod)