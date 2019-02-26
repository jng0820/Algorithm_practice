import copy

arr = []
def DFS(index, N, array):
    global arr
    if(index == N):
        return
    array2 = copy.deepcopy(array)
    array2.append(index)
    DFS(index+1,N,array2)
    arr.append(array2)
    DFS(index+1,N,array)
    
def solution(relation):
    global arr
    DFS(0,len(relation[0]),[])
    arr.sort(key=len)
    key = [0 for i in range(len(relation[0]))] 
    answer = 0
    for idx, val in enumerate(arr):
        flag = True
        for i in range(len(relation)-1):
            if(flag == False):
                break
            for j in range(i+1,len(relation)):
                check = [True for i in range(len(val))]
                for index, a in enumerate(val):
                    if(not key[a] == 0):
                        check = [False for i in range(len(val))]
                        break
                    if(relation[i][a] == relation[j][a]):
                        check[index] = False
                if(check.count(False) == len(check)):
                    flag = False
                    break
        if(flag):
            for value in val:
                key[value] = idx
            answer += 1
    print(key)
    return answer

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], 
["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], 
["600", "apeach", "music", "2"]]))