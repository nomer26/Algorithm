from bisect import bisect_left
n = int(input())
elec = []
for _ in range(n):
    a,b = map(int,input().split())
    elec.append((a,b))
elec.sort(key=lambda x:x[1])
elec = [i[0] for i in elec]

def LIS_length(arr):
    dp = [-float('inf')]
    index = [-1]*(len(arr))
    for i in range(len(arr)):
        if dp[-1]<arr[i]:
            dp.append(arr[i])
            index[i] = len(dp)-1
        else:
            ln = bisect_left(dp,arr[i])
            dp[ln] = arr[i]
            index[i] = ln
    return len(dp)-1
print(n - LIS_length(elec))