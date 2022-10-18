'''1로 만들기 - 보텀업(상향식)'''
# x = int(input())
# d = [0] * 30001
#
# for i in range(2, x+1) :
#     d[i] = d[i-1] + 1
#     if i % 2 == 0 :
#         d[i] = min(d[i], d[i//2] + 1)
#     if i % 3 == 0 :
#         d[i] = min(d[i], d[i//3] + 1)
#     if i % 5 == 0 :
#         d[i] = min(d[i], d[i//5] + 1)
# print(d[x])

'''개미 전사 - 보텀업(상향식)'''
# n = int(input())
# data = list(map(int, input().split()))
#
# d = [0] * 100
# d[0] = data[0]
# d[1] = max(data[0], data[1])
#
# for i in range(2, n) :
#     d[i] = max(d[i-1], d[i-2] + data[i])
#
# print(d[n-1]) #index로 계산해서 -1

'''바닥 공사 - 보텀업(상향식)'''

# n = int(input())
# d = [0] * 1001
#
# d[1] = 1
# d[2] = 3
# for i in range(3, n+1):
#     d[i] = (d[i-1] + 2*d[i-2]) % 796796
#
# print(d[n])

'''효율적인 화폐구성'''
n, m = map(int, input().split())
money = []

for _ in range(n) :
    money.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in money :
    for j in range(i, m+1) :
        if d[j - i] != 10001 :
            d[j] = min(d[j], d[j - i] + 1)

if d[m] != 10001 :
    print(d[m])
else :
    print(-1)