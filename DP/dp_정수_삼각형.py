'''정수 삼각형'''
n = int(input())
data = []
for _ in range(n) :
    data.append(list(map(int,input().split())))

for i in range(1, n) :
    for j in range(i+1) :
        left = 0; right = 0
        if j > 0 :
            left = data[i-1][j-1]
        if i > j :
            right = data[i-1][j]

        data[i][j] = max(left, right) + data[i][j]

print(max(data[n-1]))