a,b = input(),input()
n,m = len(a),len(b)
dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        dp[i][j] = dp[i-1][j-1]+1 if a[i-1]==b[j-1] else max(dp[i-1][j],dp[i][j-1])
ans = ''
print(dp[n][m])
if dp[n][m]!=0:
    while dp[n][m]:
        if a[n-1]==b[m-1]:
            n-=1
            m-=1
            ans+=a[n]
        elif dp[n][m]==dp[n][m-1]:
            m-=1
        else:
            n-=1
    print(ans[::-1])

