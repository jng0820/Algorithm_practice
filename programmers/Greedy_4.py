def solution(people, limit):
    answer = 1
    people.sort()
    boat_weight = 0
    number = 0
    N = len(people)
    boat = [0 for i in range(N)]
    for i in range(N):
        if(number < 2 and people[i] + boat_weight <= limit):
            boat_weight += people[i]
            number += 1
            boat[i] = answer
            if(number == 2):
                number = 0
                boat_weight = 0
                answer += 1
        else:
            boat_weight = people[i]
            answer += 1
            number = 0
            boat[i] = answer
    return answer

if __name__ == '__main__':
    print(solution([70, 80, 50], 100))