N = int(input())


arr = [0 for i in range(N+5)]
arr[2] = 1
arr[5] = 1

for i in range(7,N+1):
    val1 = arr[i-2] + 1
    val2 = arr[i-5] + 1
    if(val1 > 1 and val2 > 1):
        arr[i] = min(val1,val2)
    elif(val1 > 1):
        arr[i] = val1
    elif(val2> 1):
        arr[i] = val2

if(arr[N] == 0):
    arr[N] = -1
    
print(arr[N])