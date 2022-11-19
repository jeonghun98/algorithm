#직사각형 네개의 합집합의 면적 구하기 - 구현
data = [[False] * 101 for _ in range(101)]
for _ in range(4) :
    a,b,c,d = map(int, input().split())
    for i in range(a,c) :
        for j in range(b,d) :
            data[i][j] = True
count = 0
for i in range(1,101) :
    for j in range(1,101) :
        if data[i][j]: count += 1
print(count)