import copy

answer = 10000
arr = []
idx_arr = []
for i in range(10):
    # temp = map(int,input().split())
    temp = input().split()
    for j in range(10):
        idx_arr.append([i,j])
    temp = [int(val) for val in temp]
    arr.append(temp)
        
sticker = [5 for i in range(5)]

def fill(y,x,arr2):
    for idx in range(5,0,-1):
        cnt = 0
        if(y+idx > 10 or x+idx >10):
            continue
        for i in range(y,y+idx):
            for j in range(x,x+idx):
                if arr2[i][j] == 1:
                    cnt += 1
        if(cnt == idx*idx):
            return idx
    return -1
    
def makezero(y,x,idx,arr2):
    for i in range(y,y+idx):
        for j in range(x,x+idx):
            arr2[i][j] = 0



def DFS(idx,one,two,three,four,five,array,use):
    global answer
    global idx_arr
    count = 0
    st_cnt = 0
    if(use >= answer):
        return
    if(idx > 100):
        return
    for i in range(10):
        count += array[i].count(1)
    if(one < 0 or two < 0 or three < 0 or four < 0 or five < 0):
        return
    if(count == 0):
        answer = min(answer,use)
        return
    y,x = idx_arr[idx]
    if(array[y][x] == 0):
        DFS(idx+1,one,two,three,four,five,array,use)
        return
    ans = fill(y,x,array)
    arr2 = copy.deepcopy(array)
    if(ans == 1):
        arr2 = copy.deepcopy(array)
        makezero(y,x,1,arr2)
        DFS(idx+1,one-1,two,three,four,five,arr2,use+1)
    elif(ans == 2):
        arr2 = copy.deepcopy(array)
        makezero(y,x,2,arr2)
        DFS(idx+2,one,two-1,three,four,five,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,1,arr2)
        DFS(idx+1,one-1,two,three,four,five,arr2,use+1)
    elif(ans == 3):
        arr2 = copy.deepcopy(array)
        makezero(y,x,3,arr2)
        DFS(idx+3,one,two,three-1,four,five,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,2,arr2)
        DFS(idx+2,one,two-1,three,four,five,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,1,arr2)
        DFS(idx+1,one-1,two,three,four,five,arr2,use+1)
    elif(ans == 4):
        arr2 = copy.deepcopy(array)
        makezero(y,x,4,arr2)
        DFS(idx+4,one,two,three,four-1,five,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,3,arr2)
        DFS(idx+3,one,two,three-1,four,five,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,2,arr2)
        DFS(idx+2,one,two-1,three,four,five,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,1,arr2)
        DFS(idx+1,one-1,two,three,four,five,arr2,use+1)
    elif(ans == 5):
        arr2 = copy.deepcopy(array)
        makezero(y,x,5,arr2)
        DFS(idx+5,one,two,three,four,five-1,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,4,arr2)
        DFS(idx+4,one,two,three,four-1,five,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,3,arr2)
        DFS(idx+3,one,two,three-1,four,five,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,2,arr2)
        DFS(idx+2,one,two-1,three,four,five,arr2,use+1)
        arr2 = copy.deepcopy(array)
        makezero(y,x,1,arr2)
        DFS(idx+1,one-1,two,three,four,five,arr2,use+1)


DFS(0,5,5,5,5,5,arr,0)
if(answer == 10000):
    answer = -1
print(answer)