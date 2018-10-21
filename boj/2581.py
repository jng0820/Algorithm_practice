N = input()
M = input()

N = int(N)
M = int(M)
min = 10001
prime_arr = [0 for i in range(M+1)]
prime_arr[0] = 1
prime_arr[1] = 1

sum = 0
for i in range(2,int((M+1)/2)):
    if(prime_arr[i] == 1):
        continue
    factor = 2
    j = i*factor
    while(j<=M):
        if (prime_arr[j] == 0):
            prime_arr[j] = 1
        factor += 1
        j = i * factor

for i in range(N,M+1):
    if(prime_arr[i] == 0):
        if(min>i):
            min = i
        sum += i


if(min == 10001):
    print("-1")
else:
    print(sum)
    print(min)