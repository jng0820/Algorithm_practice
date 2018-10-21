import queue

def main():
    N, M, V = input().split()
    N = int(N)
    M = int(M)
    V = int(V)
    arr = [[0]*(N+1) for i in range (N+1)]

    for i in range (M):
        a, b = input().split()
        a = int(a)
        b = int(b)
        arr[a][b] = 1
        arr[b][a] = 1

    ans = []
    visit = [0 for i in range(N+1)]
    ans.append(V)
    visit[V] = 1
    DFS(arr,V,N,visit,ans)
    for i in range(len(ans)):
        print(ans[i], end=' ')
    print()

    ans = []
    ans.append(V)
    BFS(arr,V,N, ans)
    for i in range(len(ans)):
        print(ans[i], end = ' ')



def DFS(arr, start, end, visit, answer):
    if(visit.count(1) == end):
        return

    for i in range(1,end+1):
        if(arr[start][i] == 1 and visit[i] == 0):
            visit[i] = 1
            answer.append(i)
            DFS(arr, i, end, visit,answer)

def BFS(arr, start, end, answer):
    que = queue.Queue()
    que.put(start)
    visit = [0 for i in range (end+1)]
    visit[start] = 1
    while(que.empty() == False):
        vertex = que.get()
        for i in range(1, end+1):
            if(visit[i] == 0 and arr[vertex][i] == 1):
                visit[i] = 1
                que.put(i)
                answer.append(i)

if __name__ == '__main__':
    main()