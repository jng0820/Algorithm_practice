
str = []
str = input()
length = int(len(str)/10)

for i in range(length):
    arr = str[i*10:(i+1)*10]
    print(arr)

arr = str[length*10:]
print(arr)