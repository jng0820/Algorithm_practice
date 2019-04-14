#include <iostream>
#include <vector>

using namespace std;
int main(){
    int N;
    vector<int> vec;
    vector<int> ans;
    scanf("%d",&N);
    int minval = 1000000;
    for(int i=0;i<N;i++){
        int temp;
        scanf("%d",&temp);
        minval = min(minval,temp);
        vec.push_back(temp);
    }
    for(int i=1;i<=minval;i++){
        int check = 0;
        for(int j=0;j<vec.size();j++){
            if(vec[j] % i == 0){
                check += 1;
            }
        }
        if(check == N){
            ans.push_back(i);
        }
    }
    for(int i=0;i<ans.size();i++){
        printf("%d\n",ans[i]);
    }
}