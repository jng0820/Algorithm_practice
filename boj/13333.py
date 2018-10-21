N = int(input())
arr = input().split()
answer = 0
for i in range(N):
	arr[i] = int(arr[i])

arr.sort()
for i in range(arr[N-1]):
    for j in range(len(arr)):
        if(arr[j] >= i):
            check = j
            break
    if(j-1 <= i and N-j >= i):
        answer = i
    else:
        break

print(answer)