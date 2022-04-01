// 색종이 만들기 S3
#include<cstdio>
#include<numeric>
using namespace std;

int map[129][129];
int ans[2] = {0,};
int check(int x,int y,int size);
void sol(int x,int y,int size);
int main(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&map[i][j]);
        }
    }
    sol(0,0,n);
    for(int el:ans)
        printf("%d\n",el);
}
void sol(int x,int y,int size){
    if(size==1){ans[map[x][y]]++;return;}
    int ret = check(x,y,size);
    if(ret!=0){ans[map[x][y]]++;return;}
    size/=2;
    sol(x,y,size);
    sol(x,y+size,size);
    sol(x+size,y,size);
    sol(x+size,y+size,size);
    return;
}
int check(int x,int y,int size){
    int sum = 0;
    for(int i=x;i<x+size;i++){
        sum = accumulate(map[i]+y,map[i]+y+size,sum);
    }
    return (sum==(size*size) || sum==0) ? 1 : 0; 
}