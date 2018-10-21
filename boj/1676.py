N = int(input())

str = "1"
count = 0
for i in range(2,N+1):
    str = (int(str)*i).__str__()
    countterm = 0
    if(str[len(str)-1] == '0'):
        j = len(str)-1
        while(str[j] == '0'):
            j -= 1
            count += 1
            countterm += 1
        str = str[:-countterm]
    if(len(str)>10):
        str = str[5:]


print(count)