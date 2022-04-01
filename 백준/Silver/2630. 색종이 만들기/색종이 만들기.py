n = int(input())
data = [[*map(int,input().split())] for _ in range(n)]

def check(x,y,size):
    sub = 0
    for i in range(x,x+size):
        sub+=sum(data[i][y:y+size])
    if sub==0:
        return -1
    return sub==(size**2)     # 크기 비교

def sol(x,y,size):
    global arr
    if size==1:
        arr[data[x][y]]+=1
        return
    res = check(x,y,size)
    if res:
        arr[(res+1)//2]+=1
        return
    size//=2
    sol(x,y,size)             # 1사분면
    sol(x,y+size,size)        #  4  ''
    sol(x+size,y,size)        #  2  ''
    sol(x+size,y+size,size)   #  3  ''
    return 
arr = [0]*2
sol(0,0,n)
print(*arr,sep='\n')
