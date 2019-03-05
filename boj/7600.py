while True:
    temp = input()
    if(temp == '#'):
        break
    arr = {}
    for val in temp:
        if(val.isalpha()):
            arr[val.lower()] = 1
    print(len(arr.keys()))