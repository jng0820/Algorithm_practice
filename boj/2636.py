if __name__ == '__main__':
    N,M = input().split()
    N = int(N)
    M = int(M)
    arr = [[0 for j in range(M)] for i in range(N)]
    check = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        arr[i] = input().split()

    for i in range(N):
        for j in range(M):
            arr[i][j] = int(arr[i][j])

    sum = 0
    for i in range(N):
        for j in range(M):
            if(not arr[i][j] == 0):
                sum += 1

    time = 0
    deleted = 0
    while(not sum == 0):
        time += 1
        sum = 0
        deleted = 0
        for i in range(N):
            for j in range(M):
                if(arr[i][j] == 0):
                    continue
                circle = arr[i-1][j] + arr[i+1][j] + arr[i][j-1] + arr[i][j+1]
                if(circle < 3):
                    check[i][j] = 1

        for i in range(N):
            for j in range(M):
                if(check[i][j] == 1):
                    arr[i][j] = 0
                    check[i][j] = 0
                    deleted += 1

        for i in range(N):
            for j in range(M):
                if(arr[i][j] == 1):
                    sum+=1

    print(time)
    print(deleted)