import operator

tc = int(input())

for t in range(tc):
    n = int(input())
    arr = {}
    for i in range(n):
        A,B = input().split()
        A = float(A)/1000
        pair = {A:B}
        arr.update(pair)

    arr2 = sorted(arr.items(), key=operator.itemgetter(1), reverse=True)
    item = list(arr2[0])
    print(item[1])
