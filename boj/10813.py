N, M = map(int,input().split())

arr = [i for i in range(N+1)]

for i in range(M):
    A, B = map(int,input().split())

    temp = arr[A]
    arr[A] = arr[B]
    arr[B] = temp

for i in range(1,N+1):
    print(arr[i],end=' ')
print()