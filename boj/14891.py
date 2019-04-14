import copy

arr = []
for i in range(4):
    temp = input()
    arr.append(temp)

N = int(input())
order = []
for i in range(N):
    temp = list(map(int,input().split()))
    order.append(temp)

def rotate(array, way, num, going):
    left = num - 1
    right = num + 1
    if(left >=0 and going >=0):
        if(array[left][2] != array[num][6]):
            rotate(array,-way,left,1)
    if(right < 4 and going <= 0):
        if(array[right][6] != array[num][2]):
            rotate(array,-way,right,-1)

    temp = ""
    if(way == 1):
        temp+=array[num][7]
        for i in range(0,7):
            temp+=array[num][i]
    else:
        for i in range(1,8):
            temp+=array[num][i]
        temp+=array[num][0]
    array[num] = copy.deepcopy(temp)

for num, way in order:
    rotate(arr,way,num-1,0)

answer = 0
if(arr[0][0] == '1'):
    answer += 1
if(arr[1][0] == '1'):
    answer += 2
if(arr[2][0] == '1'):
    answer += 4
if(arr[3][0] == '1'):
    answer += 8

print(answer)