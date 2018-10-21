import queue

N, M = 0, 0
def main():
    global N, M
    N,M = input().split(' ')
    N = int(N)
    M = int(M)
    arr = [input() for i in range(N)]
    visit = [[0]*M for i in range(N)]
    #DFS(arr, 0, 0, 1, visit)
    ans = BFS(arr,visit)
    print(ans)

def BFS(arr,visit):
    global N,M
    que = queue.Queue()
    pair = [0,0]
    move = [[0]*2 for i in range(4)]
    move[0] = [1,0]
    move[1] = [-1,0]
    move[2] = [0,1]
    move[3] = [0,-1]

    que.put(pair)
    visit[0][0] = 1
    while(que.empty() == False):
        way = que.get()
        if(way[0] == N-1 and way[1] == M-1):
            return visit[N-1][M-1]

        for i in range(4):
            nextX = way[0] + move[i][0]
            nextY = way[1] + move[i][1]
            if(nextX >= 0 and nextX <N and nextY >=0 and nextY < M and visit[nextX][nextY] == 0 and arr[nextX][nextY] == '1'):
                visit[nextX][nextY] = visit[way[0]][way[1]] + 1
                que.put([nextX,nextY])


if __name__ == '__main__':
    main()