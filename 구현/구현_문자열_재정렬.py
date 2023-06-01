# 08 문자열 재정렬
data = input()
result = []
num = 0
for i in data :
    if i.isalpha() :
        result.append(i)
    else :
        num += int(i)

result.sort()
if num > 0 :
    result.append(str(num))
print(''.join(result))
