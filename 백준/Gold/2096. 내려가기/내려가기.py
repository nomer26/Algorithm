import sys;input = sys.stdin.readline
n = int(input())
mn = mx = [*map(int,input().split())] 
for i in range(n-1):
    a,b,c = map(int,input().split())
    mx0 = a + max(mx[0],mx[1])
    mn0 = a + min(mn[0],mn[1])
    mx1 = b + max(mx[0],mx[1],mx[2])
    mn1 = b + min(mn[0],mn[1],mn[2])
    mx2 = c + max(mx[1],mx[2])
    mn2 = c + min(mn[1],mn[2])
    mx = [mx0,mx1,mx2]
    mn = [mn0,mn1,mn2]
print(max(mx),min(mn))