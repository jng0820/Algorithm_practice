# -*- coding: utf-8 -*-

import bisect

def solution(budgets, M):
    arr = []
    budgets.sort()
    sum = budgets[0]
    arr.append(budgets[0]*len(budgets))
    for i in range(1,len(budgets)):
        arr.append(sum+budgets[i] * (len(budgets)-i))
        sum += budgets[i]
    idx = bisect.bisect(arr,M)
    sum = 0
    if(idx == len(budgets)):
        return budgets[len(budgets)-1]
    if(idx == 0):
        return int(M/len(budgets))

    for i in range(0,idx):
        sum += budgets[i]

    upper_value = (M - sum)/(len(budgets)-idx)
    return int(upper_value)


if __name__ == '__main__':
    print(solution([120, 110, 140, 150], 270000))