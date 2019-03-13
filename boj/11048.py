N, M = map(int,input().split())

arr = []
for i in range(N):
    temp = input().split()
    temp = [int(val) for val in temp]
    arr.append(temp)
    
DP = [[0 for i in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        if(i == 0):
            if(j == 0):
                DP[i][j] = arr[i][j]
            else:
                DP[i][j] = DP[i][j-1] + arr[i][j]
        else:
            if(j == 0):
                DP[i][j] = DP[i-1][j] + arr[i][j]
            else:
                DP[i][j] = max(DP[i-1][j],DP[i][j-1],DP[i-1][j-1]) + arr[i][j]


print(DP[N-1][M-1])