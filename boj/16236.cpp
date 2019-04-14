#include <iostream>
#include <vector>
#include <queue>

using namespace std;
typedef struct{
    int x;
    int y;
    int eat;
    int size;
}Shark;
int main(){
    int N;
    int arr[20][20];
    Shark shark;
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            scanf("%d",&arr[i][j]);
            if(arr[i][j] == 9)
            {
                shark.y = i;
                shark.x = j;
                shark.size = 2;
                shark.eat = 0;
                arr[i][j] = 0;
            }
        }
    }
    int answer = 0;
    int move[][2] ={
        {-1,0},
        {0,-1},
        {0,1},
        {1,0}
    };
    while(true){
        int y = shark.y;
        int x = shark.x;
        queue<vector<int>> q;
        bool found = false;
        vector<int> p;
        p.push_back(y);
        p.push_back(x);
        p.push_back(1);
        q.push(p);
        int visit[20][20] = {0};
        int move_now = 1;
        while(!q.empty()){
            y = q.front()[0];
            x = q.front()[1];
            move_now = q.front()[2];
            q.pop();
            visit[y][x] = 1;
            for(int i = 0; i<4;i++){
                int newy = y+move[i][0];
                int newx = x+move[i][1];
                if(newy < 0 || newx< 0 || newx == N || newy == N)
                    continue;
                if(visit[newy][newx])
                    continue;
                if(arr[newy][newx] != 0 && arr[newy][newx] <shark.size){
                    found = true;
                    shark.y = newy;
                    shark.x = newx;
                    shark.eat += 1;
                    arr[newy][newx] = 0;
                    if(shark.eat == shark.size)
                    {
                        shark.eat = 0;
                        shark.size +=1;
                    }
                    // for(int i=0;i<N;i++){
                    //     for(int j=0;j<N;j++){
                    //         printf("%d",arr[i][j]);
                    //     }
                    //     printf("\n");
                    // }
                    // printf("\n");
                    break;
                }
                else if(arr[newy][newx] == shark.size || arr[newy][newx] == 0 ){
                    vector<int> p2;
                    p2.push_back(newy);
                    p2.push_back(newx);
                    p2.push_back(move_now+1);
                    q.push(p2);
                }
            }
            if(found == true){
                answer += move_now;
                break;
            }
        }
        if(found == false){
            break;
        }
    }
    printf("%d\n",answer);
}