# 03 문자열 뒤집기
# 백준 1439번
data = input()

count1 = 0
count0 = 0

if int(data[0]) == 0 :
    count0 += 1
else :
    count1 += 1

for i in range(1,len(data)) :
    if data[i-1] != data[i]:
        if data[i] == '0' :   # 1 -> 0
            count0 += 1
        else :              # 0 -> 1
            count1 += 1
print(min(count1, count0))