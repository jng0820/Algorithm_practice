def DFS(visit, idx, computers, n, network):
    if(idx == n):
        return
    if(not (visit[idx] == 0)):
        return
    visit[idx] = network
    for i in range(n):
        if(visit[i] == 0 and computers[idx][i]):
            DFS(visit,i,computers,n,network)

def solution(n, computers):
    network = 1
    visit = [0 for i in range(n)]
    for i in range(n):
        DFS(visit,i,computers,n,network)
        network += 1
    visit.sort(reverse=True)
    arr = {}
    for i in range(len(visit)):
        arr[visit[i]] = 1

    answer = len(arr)
    return answer

if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
