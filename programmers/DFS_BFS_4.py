answer = []

def DFS(arr,idx, value):
    global answer
    answer.append(idx)
    if(not idx in arr):
        return
    for i in range(len(value)):
        if((arr[idx][i][1] == 0)):
            arr[idx][i][1] = 1
            if(value[i][0] in arr):
                DFS(arr,value[i][0],arr[value[i][0]])
            else:
                DFS(arr,value[i][0],0)

def solution(tickets):
    global visit
    arr = {}
    N = len(tickets)
    for i in range(N):
        arr[tickets[i][0]] = []
    for i in range(N):
        arr[tickets[i][0]].append([tickets[i][1],0])
    for i in range(N):
        arr[tickets[i][0]].sort(key=lambda x: x[0])
    for k, v in arr.items():
        if (not (k in arr)):
            continue
        sum = 0
        for i in range(len(arr[k])):
            sum += arr[k][i][1]

        if (sum == len(arr[k])):
            continue
        DFS(arr,k,v);
    return answer


if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
