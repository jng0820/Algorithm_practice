tc = input()
tc = int(tc)

for t in range(tc):
    k = input()
    k = int(k)
    n = input()
    n = int(n)
    str = []
    for i in range(n):
        str.append(i)

    answer = [[0 for i in range (n+1)]for j in range(k+1)]
    for i in range(k+1):
        for j in range(1,n+1):
            if i == 0:
                answer[i][j] = j
            elif j == 1:
                answer[i][j] = 1
            else:
                answer[i][j] = answer[i][j-1] + answer[i-1][j]

    print(answer[k][n])