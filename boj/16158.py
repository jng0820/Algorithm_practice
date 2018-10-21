in_arr = input().split()
N = int(in_arr[0])
X = int(in_arr[1])
K = int(in_arr[2])

ans = 0

arr = input().split()
for i in range(N):
    arr[i] = int(arr[i])

idx = 0
ans = 0
value = arr[K-1]

happy_arr = [[0 for i in range(N)]for i in range(101)]
for i in range(N):
    value = arr[i]
    for j in range(1,101):
        happy = ((value-(abs(value-j)))/value) * 100
        if(happy>=X):
            happy_arr[j][i] = happy

for i in range(1,101):
    if(happy_arr[i].count(0) == N-K):
        idx = i
        break

if(idx == 0):
    print("-1")
else:
    small = 100
    for i in range(N):
        if(happy_arr[idx][i] > X and small > happy_arr[idx][i]):
            small = happy_arr[idx][i]
    if((small/1.).is_integer() == True):
        print(idx)
    else:
        print("sex")

'''
for i in range(1,101):
    happy = ((value - (abs(value - i))) / value) * 100
    if(happy == X):
        ans = i
        break
    if(happy > X):
        idx = i
        break

if(not ans == 0):
    print(ans)
elif(ans == 0 and idx == 0):
    print(-1)
else:
    print(idx)

'''