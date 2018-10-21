def dijkstra():


    dist[start] = 0; // 시작점의
    거리
    0

    for (i =1;i <= n; i++)
    {
        min = INF;

    for ( j =1; j <= n; j++)
    {
    if ( visit[j] == 0 & & min > dist[j]) // 갈수 있는 정점중에 가장 가까운 정점 선택
    {
    min = dist[j];
    v = j;
    }
    }

    visit[v] = 1; // 가장 가까운 정점으로 방문, i정점에서 가장 가까운 최단경로 v

    for ( j = 1;j <= n; j++)
    {
    if ( dist[j] > dist[v] + a[v][j]) // 방문한 정점을 통해 다른 정점까지의 거리가 짧아지는지 계산하여 누적된값 저장
    dist[j] = dist[v] + a[v][j];
    }
    }
    }

    출처: http: // kaspyx.tistory.com / 64[잘지내나요, 내청춘]

N, M = input().split()
N = int(N)
M = int(M)

start = int(input())

arr = [[0 for i in range (N+1)]for j in range(N+1)]

for i in range(M):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    arr[a][b] = c
    arr[b][a] = c

