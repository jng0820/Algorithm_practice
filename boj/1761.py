def floyd(arr,N):
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                    arr[i][j] = arr[i][j] if arr[i][j] < arr[i][k] + arr[k][j] else arr[i][k] + arr[k][j]


N = int(input())

arr = [[10001 for i in range (N+1)]for j in range (N+1)]

for i in range(N-1):
    M = input().split()
    arr[int(M[0])][int(M[1])] = int(M[2])
    arr[int(M[1])][int(M[0])] = int(M[2])

floyd(arr,N)

K = int(input())

for i in range(K):
    node = input().split()
    node[0] = int(node[0])
    node[1] = int(node[1])
    print(arr[node[0]][node[1]])