# 설탕배달
n = int(input())
INF = int(1e9)
d = [INF] * (n+1)

for i in range(1,n+1) :
    k = INF
    if i == 3 : d[i] = 1
    if i == 5: d[i] = 1

    if i // 3 > 0 and d[i-3] < INF:
        k = min(d[i-3]+1, k)
    if i // 5 > 0 and d[i-5] < INF:
        k = min(d[i-5]+1, k)
    if k < INF :
        d[i] = k
#print(d)
if d[n] >= INF :
    print(-1)
else :
    print(d[n])