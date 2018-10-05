def solution(array, commands):
    answer = []
    answer2 = []
    for i in range(len(commands)):
        j = commands[i][0]-1
        k = commands[i][1]
        l = commands[i][2]-1
        answer = array[j:k]
        answer.sort()
        answer2.append(answer[l])
    return answer2


if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
