# LIS
# 1) 문자열들을 입력받고 각 길이를 저장
# 2) 각 문자열의 길이만큼의 2차원 dp배열을 생성
# 3) 첫번째 문자열에 대해 순회하며 두번째 문자열과 일치여부를 판단
#     3-1) 일치한다면 i-1,j-1 구간에 +1
#     3-2) 일치하지 않으면  (i,j)(i-1,j)(i,j-1) 구간에 대해 최대값         


f_str = input()
s_str = input()
f = len(f_str)
s = len(s_str)
dp = [[0 for _ in range(s+1)] for _ in range(f+1)]

for i,f_s in enumerate(f_str,1):
    for j,s_s in enumerate(s_str,1):
        if f_s==s_s:
            dp[i][j] = dp[i-1][j-1]+1
        dp[i][j] = max(dp[i][j],dp[i-1][j],dp[i][j-1])
print(dp[f][s])
