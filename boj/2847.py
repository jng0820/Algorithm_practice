N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.reverse()
count = 0
for i in range(1,N):
    while(arr[i-1]<=arr[i]):
        count += 1
        arr[i] -= 1

print(count)