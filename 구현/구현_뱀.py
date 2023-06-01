'''https://www.acmicpc.net/problem/3190 - 뱀 '''

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(k) :
    x, y = map(int,input().split())
    data[x][y] = 9
l = int(input())
move = []
for i in range(l) :
    move.append(list(input().split()))

x = 1
y = 1
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
#    동 북 서 남
dir = 0 #왼 +1 , 오 -1
time = 0
move_i = 0
move_len = len(move)
snack = [[1,1]]


while True :
    data[x][y] = 1
    n_x = dx[dir] + x
    n_y = dy[dir] + y
    if(n_x > n or n_x < 1 or n_y > n or n_y < 1 or data[n_x][n_y] == 1) :
        time += 1
        break;
    if (data[n_x][n_y] != 9):
        x0, y0 = snack.pop(0)
        data[x0][y0] = 0

    time += 1
    x = n_x
    y = n_y
    data[x][y] = 1
    snack.append([x,y])

    if(move_len > move_i and int(move[move_i][0]) == time) :
        if move[move_i][1] == 'L' :
            dir = (dir + 1) % 4
            # print(f'dir : {dir}')
            move_i += 1
        elif move[move_i][1] == 'D' :
            dir -= 1
            if(dir == -1) : dir = 3
            # print(f'dir : {dir}')
            move_i += 1
    # for i in range(n):
    #     for j in range(n):
    #         print(data[i][j], end=' ')
    #     print()
    # print("--------------------------")
print(time)