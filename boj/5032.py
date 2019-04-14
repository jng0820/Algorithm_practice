import math

A, B, C = map(int,input().split())

value = A+B 
answer = 0
while(value >= C):
    answer += math.floor(value/C)
    value = value % C + math.floor(value/C)

print(answer)