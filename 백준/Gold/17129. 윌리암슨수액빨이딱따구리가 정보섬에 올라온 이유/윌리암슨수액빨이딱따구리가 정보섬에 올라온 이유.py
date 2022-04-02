import sys; input =sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
graph = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j,num in enumerate(input().rstrip()):
        graph[i][j]=int(num)
        if num=='2':
            start = (i,j)
            visited[i][j]=True
            graph[i][j]=0
            
q = deque()
time = 0
q.append((*start,time))
while q:
    x,y,time = q.popleft()
    if graph[x][y]!=0:
        print("TAK")
        print(time)
        exit()
    for dx,dy in (0,1),(1,0),(-1,0),(0,-1):
        nx = x+dx
        ny = y+dy
        if nx<0 or ny<0 or nx>=n or ny>=m or visited[nx][ny] or graph[nx][ny]==1:continue
        visited[nx][ny]=True
        q.append((nx,ny,time+1))
print("NIE")