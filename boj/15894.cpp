#include <iostream>
#include <vector>

using namespace std;
int main(){
    int N;
    scanf("%d",&N);
    int A = 4;
    int B = 8;
    int C;
    if(N == 1){
        printf("%d\n",A);
    }
    else if(N == 2){
        printf("%d\n",B);
    }
    else{
        for(int i=2;i<N;i++){
        C = A+B;
        int temp = A;
        A = B;
        B = A;
        B = C;
    }
    printf("%d\n",C);
    }
}