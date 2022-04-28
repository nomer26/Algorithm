import sys; input =sys.stdin.readline
n = int(input())
scv = [*map(int,input().split())] +[0]*(3-n)
dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
def sol(s,c,v):
    if s<=0 and c<=0 and v<=0: return 0
    if s<=0:s=0
    if c<=0:c=0
    if v<=0:v=0
    if dp[s][c][v]:return dp[s][c][v]
    dp[s][c][v] = float('inf')
    dp[s][c][v] = min(dp[s][c][v],sol(s-9,c-3,v-1)+1)
    dp[s][c][v] = min(dp[s][c][v],sol(s-9,v-3,c-1)+1)
    dp[s][c][v] = min(dp[s][c][v],sol(c-9,s-3,v-1)+1)
    dp[s][c][v] = min(dp[s][c][v],sol(c-9,v-3,s-1)+1)
    dp[s][c][v] = min(dp[s][c][v],sol(v-9,s-3,c-1)+1)
    dp[s][c][v] = min(dp[s][c][v],sol(v-9,c-3,s-1)+1)
    return dp[s][c][v]
print(sol(scv[0],scv[1],scv[2]))