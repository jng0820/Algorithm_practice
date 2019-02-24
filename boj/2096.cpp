#include <stdio.h>

int max(int a,int b){
    return a > b ? a:b;
}
int min(int a,int b){
    return a > b ? b:a;
}

int main(){
    int N;
    scanf("%d",&N);
    printf("%d",N);
    int arr[3];
    int DP1[2][3] = {0};
    int DP2[2][3] = {0};
    for(int i=0;i<N;i++){
        scanf("%d %d %d",&arr[0],&arr[1],&arr[2]);

        DP1[1][0] = max(DP1[0][0],DP1[0][1]) + arr[0];
        DP1[1][1] = max(DP1[0][1],max(DP1[0][1],DP1[0][2])) + arr[1];
        DP1[1][2] = max(DP1[0][2],DP1[0][1]) + arr[2];

        DP2[1][0] = min(DP2[0][0],DP2[0][1]) + arr[0];
        DP2[1][1] = min(DP2[0][1],min(DP2[0][1],DP2[0][2])) + arr[1];
        DP2[1][2] = min(DP2[0][2],DP2[0][1]) + arr[2];

        for(int j=0;i<3;j++){
            DP1[0][0] = DP1[1][0];
            DP1[0][2] = DP1[1][1];
            DP1[0][3] = DP1[1][2];

            DP2[0][0] = DP2[1][0];
            DP2[0][2] = DP2[1][1];
            DP2[0][3] = DP2[1][2];
        }
    }
    printf("%d %d\n",max(DP1[1][0],max(DP1[1][1],DP1[1][2])),min(DP2[1][0],min(DP2[1][1],DP2[1][2])));
}
