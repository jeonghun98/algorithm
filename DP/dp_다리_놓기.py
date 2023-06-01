# 다리 놓기
t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    if m != n and n != 1:
        d = [0] * (m + 1)
        for i in range(1,m+1) :
            if i == 1 : d[i] = 1
            else : d[i] = d[i-1] * i

    if n == 1 :
        result = m
    elif m == n :
        result = 1
    else :
        result = d[m] // d[m - n] // d[n]

    print(result)