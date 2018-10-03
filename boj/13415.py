N = int(input())
arr = input().split()
for i in range(N):
    arr[i] = int(arr[i])
K = int(input())

for i in range(K):
    A, B = input().split()
    A = int(A)
    B = int(B)
    arr_sub = []
    arr_sub = arr[0:A]
    arr_sub.sort()
    arr[0:A] = arr_sub
    arr_sub.clear()
    arr_sub = arr[0:B]
    arr_sub.sort(reverse=True)
    arr[0:B] = arr_sub

print(arr)