def solution(numbers):
    answer = 0
    arr = []
    for i in range(len(numbers)):
        arr.append(numbers[i])
    arr.sort(reverse=True)
    max_num = ''
    for i in range(len(numbers)):
        max_num += arr[i]

    num = int(max_num)
    arr.clear()
    arr = [0 for i in range(num)+1]
    for i in range()
    return answer

if __name__ == '__main__':
    print(solution("17"))