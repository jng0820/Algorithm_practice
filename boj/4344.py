
N = int(input())
for i in range(N):
    arr = input().split()
    x = int(arr[0])
    arr.pop(0)
    sum = 0
    for j in range(x):
        arr[j] = int(arr[j])
        sum += arr[j]
    avg = sum/len(arr)
    count = 0
    for j in range(x):
        if(arr[j]>avg):
            count += 1
    print("{0:.3f}%".format(count/x*100))