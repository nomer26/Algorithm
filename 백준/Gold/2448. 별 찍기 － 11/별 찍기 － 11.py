n = int(input())
stars = [[' ']*(2*n) for _ in range(n)]

def sol(x,y,size):
    if size==3:
        stars[x][y]='*'
        stars[x+1][y-1] = stars[x+1][y+1] = '*'
        for i in range(-2,3):
            stars[x+2][y+i] ='*'
        return
    half = size//2
    sol(x,y,half)
    sol(x+half,y-half,half)
    sol(x+half,y+half,half)

sol(0,n-1,n)
for i in stars:
    print("".join(i))
