#include <queue>
#include <iostream>

using namespace std;
int main(){
    int N,M;
    scanf("%d %d",&N,&M);
}

import queue
import copy
from itertools import combinations

N,M = map(int,input().split())
arr = []
virus = []
zero = []
for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(M):
        if(temp[j] == 2):
            virus.append([i,j])
        if(temp[j] == 0):
            zero.append([i,j])
    arr.append(temp)

answer = 0

candidate = list(combinations(zero,3))
move = [[-1,0],[1,0],[0,1],[0,-1]]

for a,b,c in candidate:
    arr2 = copy.deepcopy(arr)
    arr2[a[0]][a[1]] = 1
    arr2[b[0]][b[1]] = 1
    arr2[c[0]][c[1]] = 1
    queue_arr = queue.Queue()
    for y,x in virus:
        queue_arr.put([y,x])
    while(not queue_arr.empty()):
        y,x = queue_arr.get()
        for yp,xp in move:
            newy = y+yp
            newx = x+xp
            if(newy == N or newx == M or newy < 0 or newx < 0):
                continue
            if(arr2[newy][newx] == 0):
                arr2[newy][newx] = 2
                queue_arr.put([newy,newx])

    cnt = 0
    for i in range(N):
        cnt += arr2[i].count(0)

    answer = max(cnt,answer)

print(answer)