# 줄 세우기
n = int(input())
data = list(map(int, input().split()))

result = []
for i,d in enumerate(data) :
    result.append(i+1)
    for j in range(d) :
        result[i], result[i-1] = result[i-1], result[i]
        i -= 1

for i in result :
    print(i, end= " ")