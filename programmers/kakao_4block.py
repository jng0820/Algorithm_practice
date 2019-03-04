import copy

def column(matrix, i):
    return [row[i] for row in matrix]

def down(index,n,column):
    while(index < n):
        if(index == 0) and column[index] == '!':
            column[index]=''
            index += 1
            continue
        elif(column[index] == '!'):
            column[index] = ''
            for i in range(index,0,-1):
                temp = column[i]
                column[i] = column[i-1]
                column[i-1] = temp
        index += 1

    return column
                
def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    arr = copy.deepcopy(board)
    while(True):
        delete = 0
        for i in range(1,m):
            for j in range(1,n):
                if(board[i][j] == board[i-1][j-1] == board[i-1][j] == board[i][j-1] != ''):
                    arr[i][j] = arr[i-1][j-1] = arr[i-1][j] = arr[i][j-1] = '!'
                    delete += 1
        for i in range(m):
            answer += arr[i].count('!')
        if(delete == 0):
            break
        # 4개 삭제
        for i in range(n):
            arr_column = column(arr,i)
            temp = down(0,m,arr_column)
            for j in range(m):
                arr[j][i] = temp[j]
        board = copy.deepcopy(arr)
        # 내리기
    return answer

print(solution(2, 2, ["AA", "AA"]))