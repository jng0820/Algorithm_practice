N = int(input())
arr = input().split()
answer = 0
last_val = 0
for val in arr:
    if(int(val) == 0):
        last_val = 0
    else:
        last_val += 1
        answer += last_val

print(answer)