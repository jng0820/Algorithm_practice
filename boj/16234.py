import queue as q
import math

N, L ,R = map(int,input().split())

arr = []
for i in range(N):
    temp = list(map(int,input().split()))
    arr.append(temp)

answer = 0
move = [[0,1],[1,0],[0,-1],[-1,0]]
while True:
    visit = [[0 for i in range(N)] for i in range(N)]
    summation = []
    for i in range(N):
        for j in range(N):
            q_arr = q.Queue()
            connect = []
            if(visit[i][j] == 1):
                continue
            visit[i][j] = 1
            q_arr.put([i,j,arr[i][j]])
            while(not q_arr.empty()):
                y,x,val = q_arr.get()
                connect.append([y,x])
                for yp,xp in move:
                    newx = x+xp
                    newy = y+yp
                    if(newx == N or newy == N or newx < 0 or newy < 0):
                        continue
                    if(visit[newy][newx] == 1):
                        continue
                    if(abs(arr[newy][newx]-val) >= L and abs(arr[newy][newx]-val) <= R):
                        q_arr.put([newy,newx,arr[newy][newx]])
                        visit[newy][newx] = 1
            if(len(connect)>1):
                summation.append(connect)
    #국경 철폐
    
    if(len(summation) == 0):
        break

    for val in summation:
        sum_val = 0
        cnt = len(val)
        for y,x in val:
            sum_val += arr[y][x]
        value = math.floor(sum_val / cnt)
        for y,x in val:
            arr[y][x] = value
    #인구 이동
    answer += 1

print(answer)