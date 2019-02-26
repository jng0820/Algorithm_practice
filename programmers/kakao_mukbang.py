def solution(food_times, k):
    answer = 0
    arr = [[index+1,value] for (index,value) in enumerate(food_times)]
    arr=sorted(arr,key = lambda x : x[1])
    
    time = 0
    index = 0
    while(time < k and len(arr)):
        index = arr[0][0]
        time += arr[0][1]
        del arr[0]
    
    if(time < k):
        answer = -1
    elif(time == k):
        answer = index
    else:
        answer = (time-k) % len(food_times)
    return answer

print(solution([3, 1, 2], 5))