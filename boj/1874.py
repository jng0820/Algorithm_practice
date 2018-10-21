N = input()
N = int(N)
number = []
for i in range(N):
    number.append(int(input()))

answer_str = []
stack_arr = []
s_idx = 0
n_idx = 0
for i in range(1,N+1):
    stack_arr.append(i)
    s_idx += 1
    answer_str.append("+")
    while(len(stack_arr)>0 and stack_arr[s_idx-1] == number[n_idx]):
        stack_arr.pop()
        s_idx -= 1
        n_idx += 1
        answer_str.append("-")

if(len(stack_arr) == 0):
    for i in range(len(answer_str)):
        print(answer_str[i])

else:
    print("NO")