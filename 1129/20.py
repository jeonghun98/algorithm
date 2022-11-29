# 20 감시 피하기
n = int(input())
data = []
s = []

for i in range(n) :
    temp = list(input().split())
    data.append(temp)
    for j in range(n) :
        if temp[j] == "S" :
            s.append((i,j))

def check(data) :
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(len(s)) :
        x, y = s[i][0], s[i][1]
        for j in range(4) :
            nx = x + dx[j]
            ny = y + dy[j]
            while nx >= 0 and ny >= 0 and nx < n and ny < n :
                if data[nx][ny] == "T":
                    return False
                if data[nx][ny] == "O":
                    break
                nx += dx[j]
                ny += dy[j]
    return True

result = False
def dfs(x,y,count) :
    global result
    if count == 3 :
        if check(data) :
            result = True
        return
    else :
        for i in range(n) :
            for j in range(n) :
                if i < x : continue
                if i == x and j < y : continue
                if data[i][j] == "X" :
                    data[i][j] = "O"
                    count += 1
                    dfs(i,j,count)
                    count -= 1
                    data[i][j] = "X"
dfs(0,0,0)
if result : print("YES")
else : print("NO")
