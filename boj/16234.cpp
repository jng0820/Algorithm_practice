#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;
int main(){
    int N,L,R;
    scanf("%d %d %d",&N,&L,&R);
    int arr[50][50];
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    int answer = 0;
    int move[][2] = {
        {0,1},
        {1,0},
        {-1,0},
        {0,-1}
    };
    while(true){
        int visit[50][50] = {0};
        vector<vector <pair<int,int>>> group;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                vector <pair<int,int>> connected;
                queue <pair<int,int>> q;
                if(visit[i][j])
                    continue;
                visit[i][j] = 1;
                pair <int,int> p;
                p.first = i;
                p.second = j;
                q.push(p);
                while(!q.empty()){
                    int y = q.front().first;
                    int x = q.front().second;
                    connected.push_back(q.front());
                    q.pop();
                    for(int k = 0;k<4;k++){
                        int newy = y+move[k][0];
                        int newx = x+move[k][1];
                        if(newy < 0 || newx < 0 || newy == N || newx == N)
                            continue;
                        if(visit[newy][newx] == 0 && abs(arr[newy][newx]-arr[y][x]) <= R && abs(arr[newy][newx]-arr[y][x]) >= L){
                            visit[newy][newx] = 1;
                            p.first = newy;
                            p.second = newx;
                            q.push(p);
                        }
                    }
                }
                if(connected.size() > 1)
                {
                    group.push_back(connected);
                }
            }
        }

        if(group.size() == 0)
            break;

        
        for(int i=0;i<group.size();i++){
            int sum_val = 0;
            int count = 0;
            for(int j=0;j<group[i].size();j++){
                int y = group[i][j].first;
                int x = group[i][j].second;
                sum_val += arr[y][x];
                count += 1;
            }
            sum_val = floor(sum_val / count);
            for(int j=0;j<group[i].size();j++){
                int y = group[i][j].first;
                int x = group[i][j].second;
                arr[y][x] = sum_val;
            }
        }
        answer+=1;
    }
    printf("%d\n",answer);
}