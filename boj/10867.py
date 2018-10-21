N = int(input())

arr = []
arr = input().split()

for i in range(N):
    arr[i] = int(arr[i])

arr.sort()
lastone = arr[0]
print(lastone,end=' ')
for i in range(1,N):
    if(lastone == arr[i]):
        continue
    print(arr[i],end= ' ')
    lastone = arr[i]