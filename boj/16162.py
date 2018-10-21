max = 0
in_arr = input().split()
N = int(in_arr[0])
A = int(in_arr[1])
D = int(in_arr[2])
arr = input().split()
for i in range(N):
    arr[i] = int(arr[i])

for i in range(N):
    if(arr[i] == A):
        max += 1
        A = A + D



print(max)