import queue

def BFS(place,sister):
    que=queue.Queue()
    que.put([place,0])
    visit = [0 for i in range (100001)]
    while(not que.empty()):
        value = que.get()
        if(value[0] == sister):
            return value[1]
        if(value[0]-1 >= 0 and visit[value[0] - 1] == 0):
            visit[value[0]-1] = 1
            que.put([value[0] - 1, value[1] + 1])
        if (value[0]+1 <= 100000 and visit[value[0] + 1] == 0):
            visit[value[0] + 1] = 1
            que.put([value[0] + 1, value[1] + 1])
        if (value[0] * 2 <= 100000 and visit[value[0] * 2] == 0):
            visit[value[0] * 2] = 1
            que.put([value[0] * 2, value[1] + 1])

N, K = input().split()

N = int(N)
K = int(K)

ans = BFS(N,K)

print(ans)