'''
def solution(number, k):
    answer = ''
    throw = 0
    # 2중반복문 (0 ~ k-throw) 중에 가장 큰거 고르고 다음 시작위치는 가장 컸던 인덱스+1, throw = idx - len(answer)
    maxidx = -1
    while((throw < k) and (len(answer) < len(number)-k)):
        if(maxidx+1 == len(number)):
            break
        maxvalue = '-1'
        lastidx = 0
        range_len = maxidx+k-throw+2
        if(range_len > len(number)):
            range_len = len(number)
        for i in range(maxidx+1,range_len):
            if(number[i] > maxvalue):
                maxvalue = number[i]
                maxidx = i
            lastidx += 1
        if(maxidx == -1):
            maxidx = lastidx-1
            maxvalue = ''
        answer += maxvalue
        throw = maxidx+1 - len(answer)
    if(len(answer) < len(number)-k):
        for i in range(maxidx+1,len(number)):
            answer += number[i]
    return answer
'''

def solution(number, k):
    answer = ''
    arr = []
    out_idx = 0
    arr.append(number[0])
    for i in range(1,len(number)):
        lastidx = len(arr)-1
        while(arr[lastidx] < number[i] and out_idx < k):
            arr.pop()
            lastidx -=1
            out_idx += 1
            if(lastidx == -1):
                break
        arr.append(number[i])
    for i in range(len(number)-k):
        answer += arr[i]
    return answer
if __name__ == '__main__':
    print(solution("4177252841", 4))