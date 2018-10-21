from operator import attrgetter

N = int(input())

class Student:
    def __init__(self,number, score, time, second):
        self.number = number
        self.score = score
        self.time = time
        self.second = second

        def __repr__(self):
            return repr((self.number, self.score, self.time, self.second))

student_object = []
for i in range(N):
    in_arr = input().split()
    for j in range(len(in_arr)):
        in_arr[j] = int(in_arr[j])

    student_object.append(Student(i+1, in_arr[0], in_arr[1], in_arr[2]))


result = sorted(student_object, key=attrgetter('second'))
result = sorted(result, key=attrgetter('time'))
result = sorted(result, key=attrgetter('score'), reverse=True)

print(result[0].number)