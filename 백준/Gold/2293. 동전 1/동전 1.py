n,k = map(int,input().split())
coin = sorted([int(input()) for _ in range(n)])
dp =[1]+ [0]*(k)

for idx,c in enumerate(coin):
    for i in range(c,k+1):
        dp[i] = dp[i]+dp[i-c]
print(dp[k])