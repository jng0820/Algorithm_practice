def solution(clothes):
    answer = 1

    i_len = len(clothes)
    arr = {}
    for i in range(i_len):
        if(not (clothes[i][len(clothes[i]) - 1] in arr)):
            arr[clothes[i][len(clothes[i]) - 1]] = []
        for j in range(len(clothes[i])-1):
            arr[clothes[i][len(clothes[i])-1]].append(clothes[i][j])
    for i in arr.keys():
        answer *= len(arr[i])+1

    return answer-1


if __name__ == '__main__':
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
