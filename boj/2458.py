N, M = map(int,input().split())

arr = {}
for i in range(M):
    A,B = map(int,input().split())
    if(A in arr):
        arr.append(B)
    else:
        arr 