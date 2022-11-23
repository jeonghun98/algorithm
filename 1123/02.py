# 02 곱하기 혹은 더하기
data = list(input())

result = int(data[0])
for i in range(1,len(data)) :
    num = int(data[i])
    if result <= 1 or num <= 1:
        result += num
    else :
        result *= num

print(result)