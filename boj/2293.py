
N, K = input().split()

N = int(N)
K = int(K)

DP = [0 for i in range (100000)]
str = []

for i in range(N):
    str.append(int(input()))

DP[0] = 1
str.sort()
for i in range(0,N):
    for j in range(1,K+1):
        if(j >= str[i]):
            DP[j] += DP[j-str[i]]

print(DP[K])