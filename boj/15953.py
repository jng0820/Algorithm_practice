number = int(input())

for i in range(number):
    answer = 0
    arr = input().split()
    arr[0] = int(arr[0])
    arr[1] = int(arr[1])
    if(arr[0] == 0):
        answer += 0
    elif(arr[0]<=1):
        answer+= 5000000
    elif(arr[0]<=3):
        answer += 3000000
    elif(arr[0]<=6):
        answer += 2000000
    elif(arr[0]<=10):
        answer += 500000
    elif(arr[0]<=15):
        answer += 300000
    elif(arr[0]<=21):
        answer += 100000
    else:
        answer += 0

    if(arr[1] == 0):
        answer += 0
    elif(arr[1]<=1):
        answer+= 5120000
    elif(arr[1]<=3):
        answer += 2560000
    elif(arr[1]<=7):
        answer += 1280000
    elif(arr[1]<=15):
        answer += 640000
    elif(arr[1]<=31):
        answer += 320000
    else:
        answer += 0
    
    print(answer)