#include <iostream>
#include <vector>
#include <math.h>

using namespace std;
int main(){
    int N,M;
    scanf("%d %d",&N,&M);
    vector<int> vec;
    for(int i=N;i<=M;i++){
        int temp = sqrt(i);
        if(temp == sqrt(i)){
            vec.push_back(i);
        }
    }
    if(vec.size() == 0){
        printf("-1\n");
    }
    else{
    int ans = 0;
    int ans2 = M;
    for(int i=0;i<vec.size();i++){
        ans += vec[i];
        ans2 = min(ans2,vec[i]);
    }
        printf("%d\n%d\n",ans,ans2);
    }
}