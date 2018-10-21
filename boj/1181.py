leng = input()
leng = int(leng)

maxleng = 0

str = ['0' for i in range(leng+1)]

for i in range(leng):
    str[i] = input()
    if (len(str[i]) > maxleng):
        maxleng = len(str[i])

map = ['0' for i in range(maxleng+1)]


for i in range(leng):
    if(map[len(str[i])] == '0'):
        map[len(str[i])] = str[i]
    else:
        map[len(str[i])] = map[len(str[i])]+ ' ' + str[i]

str = []
for i in range(maxleng+1):
    if(map[i] == '0'):
        continue
    str = map[i].split()
    str.sort()
    before = '0'
    for j in range(len(str)):
        if(before == str[j]):
            continue
        print(str[j])
        before = str[j]
