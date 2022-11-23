# 04 만들 수 없는 금액
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 1
for i in data :
    if result < i :
        break
    result += i
print(result)