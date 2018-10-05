from functools import cmp_to_key


def compare(item1, item2):
    if item1+item2 < item2+item1:
        return 1
    elif item1+item2 > item2+item1:
        return -1
    else:
        return 0

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    numbers.sort(key=cmp_to_key(compare))
    answer = ''
    for i in range(len(numbers)):
        answer += numbers[i]
    return answer


if __name__ == '__main__':
    print(solution([3, 30, 34, 5, 9]))