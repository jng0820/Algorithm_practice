def solution(priorities, location):
    answer = 0
    arr = []
    for i in range(len(priorities)):
        arr.append([priorities[i],i]);

    size = len(arr)
    cur = 0;
    while(cur<size):
        is_Change = False
        for i in range(cur+1,size):
            if(arr[cur][0] < arr[i][0]):
                arr.append(arr[cur])
                del arr[cur]
                is_Change = True
                break
        if(is_Change == False):
            cur += 1

    for i in range(len(arr)):
        if(arr[i][1] == location):
            return i+1
    return answer

if __name__ == '__main__':
    print(solution([2,2,2,1,3,4],3))