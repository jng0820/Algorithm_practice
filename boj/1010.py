N = int(input())

def factorial(N):
    if(N <= 1):
        return 1
    return N * factorial(N-1)

for i in range(N):
    A, B = map(int,input().split())
    C = factorial(B-A)
    A = factorial(A)
    B = factorial(B)
    answer = int(B / (A*C))
    print(answer)