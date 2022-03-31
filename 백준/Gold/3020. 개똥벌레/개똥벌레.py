# 누적합 풀이

import sys;input =sys.stdin.readline
N,H = map(int,input().split())
arr = [0]*(H+1)
for i in range(N):
    k = int(input()) # 석순 길이(범위)
    if i%2==0:    # 정방향
        arr[0]+=1
        arr[k+1]-=1
    else:           # 역방향
        arr[-k]+=1

for i in range(1,len(arr)):  # 구간별 장애물 개수 산정
    arr[i]+=arr[i-1]

arr.pop()
mn = min(arr)
print(mn,arr.count(mn))