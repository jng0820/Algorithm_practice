def solution(progresses, speeds):
    answer = []
    i=0
    days = 1
    A = len(speeds)
    while(len(answer) < A):
        N = len(progresses)
        for i in range(N):
            progresses[i] += speeds[i]

        while (N > 0 and progresses[0] >= 100):
            answer.append(days)
            del progresses[0]
            del speeds[0]
            N = len(progresses)

        days += 1
    new_answer = []
    idx = 0
    last_value = answer[0]
    new_answer.append(1)
    for i in range(1,len(answer)):
        if(answer[i] == last_value):
            new_answer[idx] += 1
        else:
            last_value = answer[i]
            idx += 1
            new_answer.append(1)
    return new_answer

if __name__ == '__main__':
    print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7]))