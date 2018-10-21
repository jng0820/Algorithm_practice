import copy

N = int(input())
arr = input().split()

for i in range(N):
    arr[i] = int(arr[i])

arr2 = copy.deepcopy(arr)
arr2.sort()

for i in range(N):
    print(arr2.index(arr[i]),end=' ')

'''
import operator

N = int(input())
input_arr = input().split()
arr= {}
for i in range(N):
    pair = {i:int(input_arr[i])}
    arr.update(pair)


arr2 = sorted(arr.items(), key=operator.itemgetter(1))

for i in range(N):
    value = list(arr2[i])
    print(value[0],end=' ')

'''