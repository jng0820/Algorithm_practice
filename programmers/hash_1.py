def solution(participant, completion):
    arr = {}
    answer = ''
    for i in range (len(participant)):
        arr[participant[i]] = 0
    for i in range (len(completion)):
        arr[completion[i]] += 1

    for val in participant:
        if(arr[val] == 0):
            answer = val
            break;
        else:
            arr[val] -=1

    return answer

if __name__ == '__main__':
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
