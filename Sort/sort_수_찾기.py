# 수 찾기
n = int(input())
data=set(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
for i in num :
    if i in data : print(1)
    else : print(0)