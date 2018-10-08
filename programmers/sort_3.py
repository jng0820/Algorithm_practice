def solution(citations):
    citations.sort()
    N = len(citations)
    answer = 0
    for j in range(10000):
        up = 0
        down = 0
        for i in range(N):
            if(citations[i] <j):
                down += 1
            else:
                up = N-down
                break
        if(up>=j and down <j):
            answer = j


    return answer


if __name__ == '__main__':
    print(solution([8, 4, 5, 3, 10]))