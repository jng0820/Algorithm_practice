def solution(answers):
    answer = []
    arr = [[0 for i in range(len(answers)+10)] for i in range(3)]
    answer_arr = [0 for i in range(3)]
    arr[1][0] = 2
    arr[1][1] = 1
    arr[1][2] = 2
    arr[1][3] = 3
    arr[1][4] = 2
    arr[1][5] = 4
    arr[1][6] = 2
    arr[1][7] = 5

    arr[2][0] = 3
    arr[2][1] = 3
    arr[2][2] = 1
    arr[2][3] = 1
    arr[2][4] = 2
    arr[2][5] = 2
    arr[2][6] = 4
    arr[2][7] = 4
    arr[2][8] = 5
    arr[2][9] = 5
    # 3 3 1 1 2 2 4 4 5 5
    for i in range(len(answers)):
        arr[0][i] = i%5 +1
    for i in range(8,len(answers)):
        arr[1][i] = arr[1][i-8]
    for i in range(10,len(answers)):
        arr[2][i] = arr[2][i-10]

    for i in range(len(answers)):
        if(answers[i] == arr[0][i]):
            answer_arr[0] += 1
        if (answers[i] == arr[1][i]):
            answer_arr[1] += 1
        if (answers[i] == arr[2][i]):
            answer_arr[2] += 1

    high_num = answer_arr[0]
    high_arr = [1]
    for i in range(1,len(answer_arr)):
        if(answer_arr[i] > high_num):
            high_arr.clear()
            high_num = answer_arr[i]
            high_arr.append(i+1)
        elif(answer_arr[i] == high_num):
            high_arr.append(i+1)

    high_arr.sort()
    return high_arr

if __name__ == '__main__':
    print(solution([1, 3, 2, 4, 2]))