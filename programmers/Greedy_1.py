def solution(n, lost, reserve):
    answer = n
    arr = {}
    lost2 = []
    for i in range(len(reserve)):
        arr[reserve[i]] = 1
    for i in range(len(lost)):
        if(lost[i] in arr):
            del arr[lost[i]]
        else:
            lost2.append(lost[i])
    lost.sort()
    cant = 0
    for i in range(len(lost2)):
        if(lost2[i]-1 in arr):
            del arr[lost2[i]-1]
        elif(lost2[i]+1 in arr):
            del arr[lost2[i]+1]
        else:
            cant+=1
    return answer -cant


if __name__ == '__main__':
    print(solution(5, [2,3,4], [3,4,5]))