import copy

answer_arr = []

def DFS(index, count, arr, temp):
    if(count == 2):
        answer_arr.append(temp)
        return
    if(index == len(arr)):
        return
    temp2 = copy.deepcopy(temp)
    temp2.append(arr[index])
    DFS(index+1,count+1,arr,temp2)
    DFS(index+1,count,arr,temp)

def GCD(a,b):
    if(b>a):
        return GCD(b,a)
    else:
        if(b == 0):
            return a
        return GCD(b,a%b)

N = int(input())

for i in range(N):
    arr = input().split()
    N = arr[0]
    del arr[0]
    DFS(0,0,arr,[])
    answer = 0
    for val1, val2 in answer_arr:
        value = GCD(int(val1),int(val2))
        answer += value
    print(answer)
    answer_arr = []