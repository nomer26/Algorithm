import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    dp = [0,1,1,1]+[0 for _ in range(3,n+1)]
    for i in range(3,n+1):
        dp[i] = dp[i-2]+dp[i-3]
    print(dp[n])