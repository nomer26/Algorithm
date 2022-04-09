n = int(input())
data = [*map(int,input().split())]
dp = [[0]*21 for _ in range(n)]
dp[0][data[0]]=1
for i in range(1,n-1):
    for j in range(21):

        if j-data[i]>=0:
            dp[i][j] += dp[i-1][j-data[i]]
        if j+data[i]<21:
            dp[i][j] += dp[i-1][j+data[i]]
#print(*dp,sep='\n')
print(dp[n-2][data[-1]])