import copy

N, K = input().split()
N = int(N)
K = int(K)

str = ['0' for i in range (N)]
alphabet = [0 for i in range(26)]
max = 0
move = [[0 for i in range (2)]for j in range (4)]
move[0] = [1,0]
move[1] = [-1,0]
move[2] = [0,1]
move[3] = [0,-1]
for i in range(N):
    str[i] = input()

def DFS(x,y,alphabet,step):
    global str
    global N,K,max,move
    idx = ord(str[x][y]) - 65
    alphabet[idx] = 1
    for i in range(4):
        nextX = x + move[i][0]
        nextY = y + move[i][1]
        if(nextX >= 0 and nextX <N and nextY >=0 and nextY < N):
            nextIdx = ord(str[nextX][nextY]) - 65
            if(alphabet[nextIdx] == 0):
                max = step+1 if step+1 > max else max
                DFS(nextX,nextY,alphabet,step+1)

    alphabet[idx] = 0

DFS(0,0,alphabet,1)
print(max)