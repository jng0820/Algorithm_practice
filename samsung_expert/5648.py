# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = []
    for i in range(N):
        in_arr = []
        a, b, c, d = map(int, input().split())
        in_arr.append(a)
        in_arr.append(b)
        in_arr.append(c)
        in_arr.append(d)
        arr.append(in_arr)

    energy = 0
    # n^2으로 i~(N-1)까지, i+1~N까지 돌음 서로 만나는 방향이면 i의 에너지를 추가한 후 break

    while (len(arr) > 1):
        pop_arr = []
        for i in range(len(arr)):
            if (arr[i][2] == 0):
                arr[i][1] += 0.5
            elif (arr[i][2] == 1):
                arr[i][1] -= 0.5
            elif (arr[i][2] == 2):
                arr[i][0] -= 0.5
            else:
                arr[i][0] += 0.5

            if (arr[i][0] > 1000 or arr[i][0] < -1000 or arr[i][1] > 1000 or arr[i][1] < -1000):
                pop_arr.append(i)

        while (len(pop_arr) > 0):
            del arr[pop_arr[0] - pop_num]
            del pop_arr[0]
            pop_num += 1

        same_idx_check = {}
        for i in range(len(arr)):
            if (not ((arr[i][0] + 1000) * 2000 + arr[i][1] in same_idx_check)):
                same_idx_check[(arr[i][0] + 1000) * 2000 + arr[i][1]] = []
            same_idx_check[(arr[i][0] + 1000) * 2000 + arr[i][1]].append(i)

        for v in same_idx_check.values():
            if (len(v) > 1):
                for i in range(len(v)):
                    pop_arr.append(v[i])
                    energy += arr[v[i]][3]
        pop_num = 0
        while (len(pop_arr) > 0):
            del arr[pop_arr[0] - pop_num]
            del pop_arr[0]
            pop_num += 1

    print("#", end='')
    print(test_case, end=' ')
    print(energy)
    # ///////////////////////////////////////////////////////////////////////////////////
