from operator import eq


def solution(phone_book):
    phone_book.sort()
    answer = False
    for i in range(len(phone_book)-1):
        if(answer == True):
            break
        for j in range(i+1,len(phone_book)):
            if(len(phone_book[i]) > len(phone_book[j])):
                continue
            else:
                book = phone_book[j][0:len(phone_book[i])]
                answer = eq(book,phone_book[i])
                if(answer == True):
                    break
    return not answer

if __name__ == '__main__':
    print(solution(["911", "97625999", "91125426"]))
