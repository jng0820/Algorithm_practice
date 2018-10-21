N, M = input().split()

N = int(N)
M = int(M)

DP = [100001 for i in range (100001)]
arr = []
arr.append(0)
for i in range(N):
    arr.append(int(input()))

DP[0] = 0
arr.sort()
for i in range(1,N+1):
    for j in range(arr[i],M+1):
        DP[j] = DP[j] if DP[j] < (DP[j-arr[i]] + 1) else DP[j-arr[i]] + 1



if(DP[M] == 100001):
    DP[M] = -1

print(DP[M])