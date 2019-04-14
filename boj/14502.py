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

def DFS(y,x,arr2):
    arr2[y][x] = 2
    for yp,xp in move:
        newy = y+yp
        newx = x+xp
        if(newy < 0 or newx < 0 or newy == N or newx == M):
            continue
        if(arr2[newy][newx] == 0):
            DFS(newy,newx,arr2)
for a,b,c in candidate:
    arr2 = copy.deepcopy(arr)
    arr2[a[0]][a[1]] = 1
    arr2[b[0]][b[1]] = 1
    arr2[c[0]][c[1]] = 1
    for y,x in virus:
        DFS(y,x,arr2)
    cnt = 0
    for i in range(N):
        cnt += arr2[i].count(0)

    answer = max(cnt,answer)

print(answer)