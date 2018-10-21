A, B = input().split()
C = input()

A = int(A)
B = int(B)
C = int(C)


minute = B+C
factor = 0
if(minute/60 > 1):
    while(minute>=60):
        minute -= 60
        factor += 1

hour = A+factor
if(hour>=24):
    hour -= 24

print("{} {}".format(hour,minute))