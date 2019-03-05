words = []

def DFS(index,arr,word,n):
    global words
    if(len(word)==n):
        words.append(word)
        return
    if(index == len(arr)):
        return
    
    word += arr[index]
    DFS(index+1,arr,word,n)
    word = word[:-1]
    DFS(index+1,arr,word,n)

number = input().split()
arr = input().split()

arr.sort()
DFS(0,arr,'',int(number[0]))
answer = []
for val in words:
    mo = 0
    mo += val.count('a')
    mo += val.count('e')
    mo += val.count('i')
    mo += val.count('o')
    mo += val.count('u')
    if(mo >=1 and len(val)-val.count('aeiou')>=2):
        answer.append(val)
print(answer)