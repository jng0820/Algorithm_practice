N = int(input())

arr = [i for i in range(N+1)]
M = int(input())

for i in range(M):
    A, B = input().split()
    A = int(A)
    B = int(B)
    if(A>B or B > N or A < 1):
        continue

    value = arr[A]
    for j in range(A,B+1):
        arr[j] = value

dic = {}
for i in range(1,N+1):
    dic[arr[i]] = 1

print(len(dic))