from itertools import combinations,product
import sys; input =sys.stdin.readline
#r = open('text.txt','r')

def get_dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
n,m = map(int,input().split())
data = [[*map(int,input().split())] for _ in range(n)]
houses,kfcs,pick = [],[],[]
for i in range(n):
    for j in range(n):
        if data[i][j]==1:
            houses.append((i,j))
        elif data[i][j]==2:
            kfcs.append((i,j))
ans = float('inf')
for com in combinations(kfcs,m):
    dist = 0
    for i in range(len(houses)):
        mn_dist = float('inf')
        for j in range(len(com)):
            mn_dist = min(mn_dist,get_dist(houses[i],com[j]))
        dist += mn_dist
    ans = min(ans,dist)
print(ans)