N = int(input())

arr = []
for i in range(N):
    temp = list(map(int,input().split()))
    arr.append(temp)

answer = 0

def DFS(idx,N,value,arr):
    global answer
    if(idx ==N):
        answer = max(answer,value)
        return
    elif(idx > N):
        return
    DFS(idx+arr[idx][0],N,value + arr[idx][1],arr)
    DFS(idx+1,N,value,arr)

DFS(0,N,0,arr)
print(answer)