# 05 볼링공 고르기
n, m = map(int, input().split())
data = list(map(int, input().split()))

remain = n
result = 0
for i in range(1,m+1) :
    k = data.count(i)
    n -= k
    result += k * n
print(result)
