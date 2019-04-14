#include <iostream>
#include <vector>

using namespace std;
int answer = 987654321;
vector <pair<int,int>> idx_arr;

int arr_fill(int y,int x,vector<vector<int>> array){
    for(int idx = 5; idx >= 0; idx--){
        int cnt = 0;
        if(y+idx > 10 || x+idx > 10)
            continue;
        for(int i=y;i<y+idx;i++){
            for(int j=x;j<x+idx;j++){
                if(array[i][j] == 1)
                    cnt +=1;
            }
        }
        if(cnt == idx*idx){
            return idx;
        }
    }
    return -1;
}
void makezero(int y,int x,int idx,vector<vector<int>>&array){
    for(int i=y;i<y+idx;i++){
        for(int j=x;j<x+idx;j++){
            array[i][j] = 0;
        }
    }
}
void DFS_func(int idx,int one,int two,int three,int four,int five,vector<vector<int>>arr,int use){
    int count = 0;
    if(use >= answer)
        return;
    if(idx > 100)
        return;
    if(one < 0 or two < 0 or three < 0 or four < 0 or five < 0)
        return;
    
    for(int i=0;i<10;i++){
        for(int j=0;j<10;j++){
            if(arr[i][j] == 1){
                count++;
            }
        }
    }
    if(count == 0){
        answer = min(answer,use);
        return;
    }
    int y = idx_arr[idx].first;
    int x = idx_arr[idx].second;
    if(arr[y][x] == 0){
        DFS_func(idx+1,one,two,three,four,five,arr,use);
        return;
    }
    int ans = arr_fill(y,x,arr);
    vector<vector<int>>arr2;
    if(ans == 1){
        arr2 = arr;
        makezero(y,x,1,arr2);
        DFS_func(idx+1,one-1,two,three,four,five,arr2,use+1);
    }
    else if(ans == 2){
        arr2 = arr;
        makezero(y,x,2,arr2);
        DFS_func(idx+2,one,two-1,three,four,five,arr2,use+1);
        arr2 = arr;
        makezero(y,x,1,arr2);
        DFS_func(idx+1,one-1,two,three,four,five,arr2,use+1);
    }
    else if(ans == 3){
        arr2 = arr;
        makezero(y,x,3,arr2);
        DFS_func(idx+3,one,two,three-1,four,five,arr2,use+1);
        arr2 = arr;
        makezero(y,x,2,arr2);
        DFS_func(idx+2,one,two-1,three,four,five,arr2,use+1);
        arr2 = arr;
        makezero(y,x,1,arr2);
        DFS_func(idx+1,one-1,two,three,four,five,arr2,use+1);
    }
    else if(ans == 4){
        arr2 = arr;
        makezero(y,x,4,arr2);
        DFS_func(idx+4,one,two,three,four-1,five,arr2,use+1);
        arr2 = arr;
        makezero(y,x,3,arr2);
        DFS_func(idx+3,one,two,three-1,four,five,arr2,use+1);
        arr2 = arr;
        makezero(y,x,2,arr2);
        DFS_func(idx+2,one,two-1,three,four,five,arr2,use+1);
        arr2 = arr;
        makezero(y,x,1,arr2);
        DFS_func(idx+1,one-1,two,three,four,five,arr2,use+1);
    }
    else if(ans == 5){
        arr2 = arr;
        makezero(y,x,5,arr2);
        DFS_func(idx+5,one,two,three,four,five-1,arr2,use+1);
        arr2 = arr;
        makezero(y,x,4,arr2);
        DFS_func(idx+4,one,two,three,four-1,five,arr2,use+1);
        arr2 = arr;
        makezero(y,x,3,arr2);
        DFS_func(idx+3,one,two,three-1,four,five,arr2,use+1);
        arr2 = arr;
        makezero(y,x,2,arr2);
        DFS_func(idx+2,one,two-1,three,four,five,arr2,use+1);
        arr2 = arr;
        makezero(y,x,1,arr2);
        DFS_func(idx+1,one-1,two,three,four,five,arr2,use+1);
    }
}
int main(){
    vector <vector<int>> arr;
    for(int i=0;i<10;i++){
        vector <int>temp;
        for(int j=0;j<10;j++){
            int a;
            scanf("%d",&a);
            temp.push_back(a);
            pair<int, int>p;
            p.first = i;
            p.second = j;
            idx_arr.push_back(p);
        }
        arr.push_back(temp);
    }
    DFS_func(0,5,5,5,5,5,arr,0);
    if(answer == 987654321)
        answer = -1;
    printf("%d\n",answer);
}