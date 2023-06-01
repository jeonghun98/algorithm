# 색종이
n = int(input())
data = [[False] * 101 for _ in range(101)]
for _ in range(n) :
    x, y = map(int, input().split())
    for i in range(x, x+10) :
        for j in range(y, y+10) :
            data[i][j] = True

result = 0
for i in range(1,101) :
    for j in range(1,101) :
        if data[i][j] : result += 1
print(result)