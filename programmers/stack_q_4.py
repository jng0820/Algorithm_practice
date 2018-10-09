def solution(bridge_length, weight, truck_weights):
    answer = 0
    complete_arr = []
    bridge_arr = []
    bridge_weight = 0
    N = len(truck_weights)
    time = 1
    while(len(complete_arr) < N):
        for i in range(len(bridge_arr)):
            bridge_arr[i][0] -= 1
        if(len(bridge_arr) and bridge_arr[0][0] == 0):
            bridge_weight -= bridge_arr[0][1]
            complete_arr.append(bridge_arr[0][1])
            del bridge_arr[0]

        if(len(truck_weights) and truck_weights[0]+ bridge_weight <= weight and len(bridge_arr) != bridge_length):
            bridge_arr.append([bridge_length,truck_weights[0]])
            bridge_weight += truck_weights[0]
            del truck_weights[0]

        time += 1
    answer = time
    return answer

if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))