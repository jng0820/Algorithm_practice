str = [0 for i in range (8)]

for i in range(8):
    str[i] = input()

board = [[0]*8 for i in range(8)]

for i in range(8):
    for j in range(8):
        if(i%2 == 0):
            if(j%2 == 1):
                board[i][j] = 1
        else:
            if(j%2 == 0):
                board[i][j] = 1

count = 0
for i in range(8):
    for j in range(8):
        if(str[i][j] == 'F' and board[i][j] == 0):
            count +=1

print(count)