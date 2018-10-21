K = int(input())

for i in range(K):
    arr = input().split()
    hp = int(arr[0]) + int(arr[4])
    mp = int(arr[1]) + int(arr[5])
    att = int(arr[2]) + int(arr[6])
    defence = int(arr[3]) + int(arr[7])
    if(hp < 1):
        hp = 1
    if(mp <1):
        mp = 1
    if(att <= 0):
        att = 0

    power = hp*1 + 5*mp + 2*att + 2*defence
    print(power)