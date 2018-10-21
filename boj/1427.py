number = input()

str = []
for i in range(0,len(number)):
    str.append(int(number[i]))

str.sort(reverse=True)

for i in range(len(str)):
    print(str[i],end='')