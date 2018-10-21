
N = input()
str = []
N = int(N)
for i in range(N):
    str.append(int(input()))

str.sort()

for i in range(N):
    print(str[i],end=' ')