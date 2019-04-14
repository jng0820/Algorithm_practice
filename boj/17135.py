N, M, D = input().split()
N = int(N)
M = int(M)
D = int(D)

arr = []
for i in range(N):
    temp = input().split()
    temp = [int(val) for val in temp]
    arr.append(temp)
    