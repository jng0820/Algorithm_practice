import bisect

def solution(n, times):
    times.sort()
    l = times[0]
    r = times[len(times)-1]*n
    answer = r
    while(l<=r):
        mid = int((l+r)/2)
        sum = 0
        for i in range(len(times)):
            sum += int(mid/times[i])
        if(sum >= n):
            if(answer > mid):
                answer = mid;
            r = mid-1
        else:
            l = mid +1

    return answer


if __name__ == '__main__':
    print(solution(6, [7, 10]))