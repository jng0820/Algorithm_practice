import copy

N, L = map(int,input().split())

arr = []
for i in range(N):
    temp = list(map(int,input().split()))
    arr.append(temp)

def check(array):
    last = 0
    cnt = 0
    temp = [0 for i in range(N)]
    for i in range(N):
        if(last == 0 or last == array[i]):
            cnt += 1
        elif(last == array[i]-1):
            if(cnt >= L):
                cnt = 1
                for j in range(L):
                    temp[i-1-j] = 1
        else:
            cnt = 1
        last = array[i]
    
    cnt = 0
    last = 0
    for i in range(N-1,-1,-1):
        if(last == 0 or last == array[i]):
            cnt += 1
        elif(last == array[i]-1):
            if(cnt >= L):
                cnt = 1
                tmp_cnt = 0
                for j in range(L):
                    if(temp[i+1+j] == 0):
                        tmp_cnt += 1
                if(tmp_cnt == L):
                    for j in range(L):
                        temp[i+1+j] = -1
        else:
            cnt = 1
        last = array[i]
    
    last = array[0]
    for i in range(N):
        if(abs(last - array[i]) >1):
            return 0
        if(last > array[i] and temp[i] != -1):
            return 0
        if(last < array[i] and temp[i-1] != 1):
            return 0
        last = array[i]
    return 1

answer = 0
for i in range(N):
    answer += check(arr[i])
    tmp = []
    for j in range(N):
        tmp.append(arr[j][i])
    
    answer += check(tmp)

print(answer)