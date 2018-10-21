N = input()
number = input().split()

DP = [0 for i in range(len(number))]
max = 0

for i in range(0,len(number)):
    DP[i] = int(number[i])
    for j in range(0,i):
        if int(number[j])<int(number[i]):
            if(DP[i]<DP[j]+int(number[i])):
                DP[i] = DP[j]+int(number[i])
    max = max if max > DP[i] else DP[i]

print(max)