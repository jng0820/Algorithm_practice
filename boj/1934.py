N = int(input())

def GDC(a,b):
    if(b>a):
        return GDC(b,a)
    if(a%b == 0):
        return b
    return GDC(b,a%b)

for i in range(N):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print(int((A*B)/GDC(A,B)))