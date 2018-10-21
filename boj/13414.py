import operator

N, M = input().split()
N = int(N)
M = int(M)
arr = {}
for i in range(M):
    a = input()
    arr[a] = i

sorted_arr = sorted(arr.items(), key=operator.itemgetter(1))
for i in range(N):
    print(sorted_arr[i][0])