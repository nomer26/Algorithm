def sol_14852():
    n = int(input())
    dp =[[0 for _ in range(2)] for _ in range(n+1)]

    if n<2:
        print(n*2)
    else:
        dp[0][0] = 0
        dp[1][0] = 2
        dp[2][0] = 7
        dp[2][1] = 1
        for i in range(3,n+1):
            dp[i][1] = (dp[i-1][1] + dp[i-3][0]) % 1_000_000_007
            dp[i][0] = (2*dp[i-1][0] + 3*dp[i-2][0] + 2*dp[i][1]) % 1_000_000_007
        print(dp[n][0])
        
if __name__=='__main__':
    sol_14852()