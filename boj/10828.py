N = int(input())

arr = []
for i in range(N):
    order = input().split()
    length = len(arr)
    if(order[0] == 'push'):
        arr.append(order[1])
    elif(order[0] == 'top'):
        if(length == 0):
            print("-1")
        else:
            print(arr[length-1])
    elif(order[0] == 'empty'):
        if(length == 0):
            print(1)
        else:
            print(0)
    elif(order[0] == 'size'):
        print(length)
    else:
        if(length == 0):
            print("-1")
        else:
            print(arr[length-1])
            arr.pop()