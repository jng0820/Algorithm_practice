import copy

N = int(input())
arr = []

for i in range(N):
    temp = list(map(int,input().split()))
    arr.append(temp)

answer = 987654321

def DFS(idx,N,teamA,arr):
    global answer
    if(len(teamA) == N/2):
        teamB = []
        for i in range(N):
            if(not i in teamA):
                teamB.append(i)
        p1 = 0
        p2 = 0
        for val in teamA:
            for val2 in teamA:
                p1 += arr[val][val2]
        
        for val in teamB:
            for val2 in teamB:
                p2 += arr[val][val2]
        
                
        answer = min(answer,abs(p1-p2))
        return
    elif(idx == N):
        return
    else:
        teamA2 = copy.deepcopy(teamA)
        teamA2.append(idx)
        DFS(idx+1,N,teamA2,arr)
        teamA2 = copy.deepcopy(teamA)
        DFS(idx+1,N,teamA2,arr)

DFS(0,N,[],arr)
print(answer)