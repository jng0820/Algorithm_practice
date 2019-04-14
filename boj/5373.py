import copy

N = int(input())
cube = []

cube.append([['w','w','w'],['w','w','w'],['w','w','w']]) #상
cube.append([['r','r','r'],['r','r','r'],['r','r','r']]) #전
cube.append([['g','g','g'],['g','g','g'],['g','g','g']]) #좌
cube.append([['b','b','b'],['b','b','b'],['b','b','b']]) #우
cube.append([['y','y','y'],['y','y','y'],['y','y','y']]) #하
cube.append([['o','o','o'],['o','o','o'],['o','o','o']]) #후

def rotate_90(array,way):
    temp = copy.deepcopy(array)
    if(way == '+'):
        #012 -> 258, 258 -> 876, 876 -> 630, 630 -> 012
        temp[0][2] = array[0][0]
        temp[1][2] = array[0][1]
        temp[2][2] = array[0][2]
        temp[2][1] = array[1][2]
        temp[2][0] = array[2][2]
        temp[1][0] = array[2][1]
        temp[0][0] = array[2][0]
        temp[0][1] = array[1][0]
    else:
        #012 -> 630, 630 -> 876, 876 -> 258, 258 -> 012
        temp[2][0] = array[0][0]
        temp[1][0] = array[0][1]
        temp[0][0] = array[0][2]
        temp[2][2] = array[2][0]
        temp[2][1] = array[1][0]
        temp[0][2] = array[2][2]
        temp[1][2] = array[2][1]
        temp[0][1] = array[1][2]

    array = copy.deepcopy(temp)

def cube_rotate(cube,side,way):
    if(side == 'U'):
        if(way == '+'):
            temp = copy.deepcopy(cube[1][0])
            cube[1][0] = copy.deepcopy(cube[3][0])
            cube[3][0] = copy.deepcopy(cube[5][0])
            cube[5][0] = copy.deepcopy(cube[2][0])
            cube[2][0] = copy.deepcopy(temp)
            rotate_90(cube[0],way)
        else:

    #     #cube[1],cube[2],cube[3],cube[5]의 123을 돌림, 정방향과 역방향
    #     #cube[0] 90도 회전
    # elif(side == 'F'):
    #     #cube[0] 789,cube[2] 369,cube[3] 147,cube[4] 123 돌림, 정방향과 역방향
    #     #cube[1] 90도 회전
    # elif(side == 'L'):
    #     #cube[0] 147, cube[1] 147, cube[4] 147, cube[5] 369 돌림, 정방향과 역방향
    #     #cube[2] 90도 회전
    # elif(side == 'R'):
    #     #cube[0] 369, cube[1] 369, cube[4] 369, cube[5] 147 돌림, 정방향과 역방향
    #     #cube[3] 90도 회전
    # elif(side == 'D'):
    #     #cube[1] 789, cube[2] 789, cube[5] 789 cube[3] 789 돌림, 정방향과 역방향
    #     #cube[4] 90도 회전
    # else:
    #     #cube[0] 123, cube[3] 369, cube[4] 789, cube[1] 147 돌림, 정방향과 역방향
    #     #cube[5] 90도 회전

for i in range(N):
    A = int(input())
    order = input().split()
    for val in order:
        cube_rotate(cube,val[0],val[1])
    