# 16 연구소
#import copy
# -> deepcopy보다 이중 for문으로 copy하는게 더 빠름
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]
for _ in range(n) :
    data.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus(x,y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m : continue
        if temp[nx][ny] == 0 :
            temp[nx][ny] = 2
            virus(nx,ny)

def count_safe() :
    safe = 0
    for i in range(n):
        safe += temp[i].count(0)
        # for j in range(m) :
        #     if temp[i][j] == 0 :
        #         safe += 1
    return safe

def dfs(x,y,count) :
    global result
    if count == 3 :
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n) :
            for j in range(m) :
                if temp[i][j] == 2 :
                    virus(i,j)
        result = max(count_safe(), result)
        return
    else :
        for i in range(n) :
            for j in range(m) :
                if data[i][j] == 0:
                    if i < x : continue
                    if i == x and j < y : continue
                    data[i][j] = 1
                    count += 1
                    dfs(i,j,count)
                    count -= 1
                    data[i][j] = 0

result = 0
dfs(0,0,0)
print(result)