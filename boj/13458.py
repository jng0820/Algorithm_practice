import math

N = int(input())

arr = list(map(int,input().split()))
B,C = map(int,input().split())

arr = [val - B for val in arr]
answer = N
for val in arr:
    if(val <= 0):
        continue
    else:
        answer += math.ceil(val / C)

print(answer)