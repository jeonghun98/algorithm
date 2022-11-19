# 스위치 켜고 끄기 - 구현
n = int(input())
data = [0]
data.extend(list(map(int, input().split())))

s = int(input())
for _ in range(s) :
    a, b= map(int, input().split())
    if a == 1 :
        i = 2; num = b
        while num <= n :
            if data[num] == 1 : data[num] = 0
            else : data[num] = 1
            num = b * i; i += 1
    else :
        i = 1
        while True :
            if b-i <= 0 or b+i > n :
                break
            if data[b-i] == data[b+i] :
                i += 1
            else : break

        for j in range(i) :
            if data[b+j] == 1 :
                data[b+j] = 0; data[b-j] = 0
            else :
                data[b+j] = 1; data[b-j] = 1
    print(data)

for i in range(1,n+1) :
    if i % 20 != 0:
        print(data[i], end=" ")
    else :
        print(data[i])