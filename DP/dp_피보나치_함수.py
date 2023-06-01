# 피보나치 함수
import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc) :
    n = int(input())
    data = [[0,0] for _ in range(n+1)]
    for i in range(n+1) :
        if i == 0 : data[i][0] = 1; data[i][1] = 0
        elif i == 1 : data[i][0] = 0; data[i][1] = 1
        else :
            a, b = data[i - 1]
            c, d = data[i - 2]
            data[i][0] = a+c
            data[i][1] = b+d
    print(data[n][0], data[n][1])
