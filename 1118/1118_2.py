# 1로 만들기
n = int(input())
INF = int(1e9)
d = [INF] * (n+1)
d[0] = 0; d[1] = 0

for i in range(2,n+1) :
    d[i] = d[i-1] + 1
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])