N = input()
N = int(N)

str = input().split()
for i in range(len(str)):
    str[i] = int(str[i])

prime_number = [0 for i in range(str[len(str)-1]+1)]

prime_number[1] = 1

for i in range(2,str[len(str)-1]+1):
    if(prime_number[i] == 1):
        continue
    j = i
    factor = 2
    idx = j*factor
    while(idx <= str[len(str)-1]):
        prime_number[idx] = 1
        factor += 1
        idx = j*factor

count = 0
for i in range(len(str)):
    if(prime_number[str[i]] == 0):
        count += 1

print(count)