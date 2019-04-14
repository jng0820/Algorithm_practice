import math

N = int(input())

arr = list(map(int,input().split()))
order = list(map(int,input().split()))

max_val = -1000000000
min_val = 1000000000
def DFS(index,N,plus,minus,mul,div,val):
    global max_val,min_val
    if(index == N):
        max_val = max(max_val,val)
        min_val = min(min_val,val)
        return
    
    if(plus > 0):
        DFS(index+1,N,plus-1,minus,mul,div,val+arr[index])
    if(minus > 0):
        DFS(index+1,N,plus,minus-1,mul,div,val-arr[index])
    if(mul > 0):
        DFS(index+1,N,plus,minus,mul-1,div,val*arr[index])
    if(div > 0):
        DFS(index+1,N,plus,minus,mul,div-1,int(val/arr[index]))

DFS(1,N,order[0],order[1],order[2],order[3],arr[0])
print(max_val)
print(min_val)