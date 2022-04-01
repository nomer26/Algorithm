n,m,l = map(int,input().split())
graph = [0]+sorted([*map(int,input().split())]) + [l]

dist = 0
for i in range(1,len(graph)):
    if dist < graph[i]-graph[i-1]:
        dist = graph[i]-graph[i-1]
s,e = 1,dist
while s<=e:
    mid = (s+e)//2
    sum_ = 0
    for i in range(1,len(graph)):
        sum_+=(graph[i]-graph[i-1]-1)//mid
    if sum_<=m:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
print(ans)