import queue

N = int(input())
M = int(input())
arr = [[] for i in range(N+1)]
visit = [0 for i in range(N+1)]
for i in range(M):
    A, B = map(int,input().split())
    arr[A].append(B)
    arr[B].append(A)

q = queue.Queue()
q.put(1)

while(not q.empty()):
    index = q.get()
    if(visit[index]):
        continue
    visit[index] = 1
    for val in arr[index]:
        q.put(val)

print(visit.count(1)-1)