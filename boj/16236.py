import queue

class Shark:
    x = 0
    y = 0
    size = 0

total_fish = 0
total_eat = 0
answer = 0
N = int(input())
arr = []
shark = Shark()
shark_find = False
for i in range(N):
    temp = input().split()
    temp = [int(val) for val in temp]
    arr.append(temp)
    for index,val in enumerate(temp):
        if(val == 9):
            shark.x = index
            shark.y = i
            arr[shark.y][shark.x] = 0
            shark.size = 2
            shark_find = True
        elif(val > 0 and val < 9):
            total_fish += 1


move = [[-1,0],[0,-1],[0,1],[1,0]]
eat = 0
while(True):
    if(total_fish == total_eat):
        break

    queue_arr = queue.Queue()
    found = False
    visit = [[0 for i in range(N)] for i in range(N)] 
    queue_arr.put([shark.y,shark.x,1])
    while(not queue_arr.empty()):
        food = []
        shark_y, shark_x, move_now = queue_arr.get()
        visit[shark_y][shark_x] = 1
        for y_plus, x_plus in move:
            new_y = shark_y + y_plus
            new_x = shark_x + x_plus
            if(new_x < 0 or new_x == N or new_y < 0 or new_y == N):
                continue
            if(visit[new_y][new_x] == 1):
                continue
            if(arr[new_y][new_x] == 0 or arr[new_y][new_x] == shark.size):
                queue_arr.put([new_y,new_x,move_now+1])
            elif(arr[new_y][new_x] < shark.size):
                found = True
                eat += 1
                shark.y = new_y
                shark.x = new_x
                arr[new_y][new_x] = 0
                if(eat == shark.size):
                    shark.size += 1
                    eat = 0
                answer += move_now
                total_eat += 1
                break
        if(found == True):
            break
    if(found == False):
        break

print(answer)