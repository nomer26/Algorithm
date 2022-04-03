# 12865 (평범한 배낭)
import sys; input = sys.stdin.readline
n,k = map(int,input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for idx,(w,v) in enumerate(sorted([[*map(int,input().split())] for _ in range(n)],reverse=True),1):
    for i in range(w,k+1):
        dp[idx][i] = max(dp[idx][i-1],dp[idx-1][i],v+dp[idx-1][i-w])
print(dp[n][k])