# 수 이어가기 - 완전탐색
import copy
n = int(input())
result = []
for i in range(1,n+1) :
    data = [n,i]
    j = 2

    while True :
        i = data[j - 2] - data[j - 1]
        if i < 0 : break
        data.append(i); j += 1

    if len(result) < len(data) :
        result = copy.deepcopy(data)
print(len(result))
for i in result :
    print(i, end = " ")