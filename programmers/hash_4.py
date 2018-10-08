import operator


def solution(genres, plays):
    answer = {}
    N = len(plays)
    for i in range(N):
        answer[genres[i]] = 0
    for i in range(N):
        answer[genres[i]] += plays[i]
    sortedArr = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)
    arr = []
    for j in range(len(sortedArr)):
        sub_arr = []
        for i in range(N):
            if(operator.eq(genres[i], sortedArr[j][0])):
                sub_arr.append([plays[i],i])
        sub_arr.sort(key=lambda x: x[0],reverse=True)
        many = 0
        for i in range(len(sub_arr)):
            if(many == 2):
                break
            arr.append(sub_arr[i])
            many += 1

    new_answer = []
    for i in range(len(arr)):
        new_answer.append(arr[i][1])
    return new_answer

if __name__ == '__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))