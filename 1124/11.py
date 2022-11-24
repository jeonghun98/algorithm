# 11 뱀
from collections import deque
n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
data[1][1] = 1
for _ in range(k) :
    x, y = map(int, input().split())
    data[x][y] = 2
l = int(input())
time = []
for _ in range(l) :
    t, rl = input().split()
    time.append((int(t), rl))

q = deque()
q.append((1,1))

dir = 0
x, y= 1, 1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

count = 0; time_index = 0
while True :
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx > n or ny > n or nx < 1 or ny < 1 or data[nx][ny] == 1:
        count += 1
        break
    if data[nx][ny] == 0 :
        bx, by = q.popleft()
        data[bx][by] = 0
    x = nx; y = ny
    data[x][y] = 1
    q.append((x, y))
    count += 1
    if time_index < l and count == time[time_index][0] :
        if time[time_index][1] == "L" :
            dir -= 1
            if dir == -1 : dir = 3
        else :
            dir += 1
            if dir == 4 : dir = 0
        time_index += 1
print(count)
# for i in range(1,n+1):
#     for j in range(1, n+1) :
#         print(data[i][j], end = ' ')
#     print()