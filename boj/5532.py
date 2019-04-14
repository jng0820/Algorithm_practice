import math

N = int(input())

A = int(input())
B = int(input())
C = int(input())
D = int(input())

print(N-max(math.ceil(A/C),math.ceil(B/D)))