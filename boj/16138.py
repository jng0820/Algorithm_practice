in_arr = input().split()
minimum = int(in_arr[0])
maximum = int(in_arr[1])

N = int(input())
arr = [[0 for i in range(2)]for i in range(N)]
max = -1000000
for i in range(N):
    in_arr = input().split()
    arr[i][0] = int(in_arr[0])
    arr[i][1] = int(in_arr[1])

def DFS(index,credit,happy):
    global minimun, maximum
    global arr,N,max
    if(credit>maximum):
        return
    if(credit >= minimum and credit <= maximum):
        max = max > happy and max or happy
        return
    if(N == index):
        return
    DFS(index + 1, credit+arr[index][0],happy+arr[index][1])
    DFS(index + 1, credit, happy)

DFS(0,0,0)
print(max)