'''감시 피하기'''

from itertools import combinations
n = int(input())
data = []
teacher = []
space = []


for i in range(n) :
    data.append(list(input().split()))
    for j in range(n) :
        if data[i][j] == "T" :
            teacher.append((i,j))
        if data[i][j] == "X" :
            space.append((i,j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find(x,y) :
    for i in range(4) :
        nx = x
        ny = y
        while nx >= 0 and nx < n and ny >= 0 and ny < n :
            if data[nx][ny] == "S" :
                return True
            elif data[nx][ny] == "O" :
                break
            nx += dx[i]; ny += dy[i]
    return False

def teacher_find() :
    for x,y in teacher :
        if find(x,y) : return True
    return False

success = False
for sp in combinations(space, 3) :
    for x,y in sp :
        data[x][y] = "O"
    if not teacher_find() :
        success = True
        break
    for x, y in sp :
        data[x][y] = "X"

if success :
    print("YES")
else :
    print("NO")




