
str = input()
alphabet = [-1 for i in range(26)]

for i in range(len(str)):
    if(alphabet[ord(str[i])-97] == -1):
        alphabet[ord(str[i])-97] = i

for i in range(len(alphabet)):
    print(alphabet[i],end=' ')