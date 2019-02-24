import copy

N = int(input())

answer = []
DP1 = [[0 for i in range(3)] for i in range(2)]
DP2 = [[0 for i in range(3)] for i in range(2)]
for i in range(N):
    temp = input().split()
    temp = [int(val) for val in temp]
    
    DP1[1][0] = max(DP1[0][0],DP1[0][1]) + temp[0]
    DP1[1][1] = max(DP1[0][0],DP1[0][1],DP1[0][2]) + temp[1]
    DP1[1][2] = max(DP1[0][2],DP1[0][1]) + temp[2]

    DP2[1][0] = min(DP2[0][0],DP2[0][1]) + temp[0]
    DP2[1][1] = min(DP2[0][0],DP2[0][1],DP2[0][2]) + temp[1]
    DP2[1][2] = min(DP2[0][2],DP2[0][1]) + temp[2]

    for i in range(3):
        DP1[0][i] = DP1[1][i]
        DP2[0][i] = DP2[1][i]

print(str(max(DP1[1]))+' '+str(min(DP2[1])))
