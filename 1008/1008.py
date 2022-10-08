''' 연산자 끼워넣기 '''
n = int(input())
num = list(map(int,input().split()))
add, sub, mul, div = map(int, input().split())

max_n = -1e9
min_n = 1e9

def dfs(i, now) :
    global add, sub, mul, div, max_n, min_n
    if i == n :
        max_n = max(max_n, now)
        min_n = min(min_n, now)
    else :
        if add > 0 :
            add -= 1
            dfs(i + 1, now + num[i])
            add += 1
        if sub > 0 :
            sub -= 1
            dfs(i + 1, now - num[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i + 1, now * num[i])
            mul += 1
        if div > 0 :
            div -= 1
            dfs(i + 1, int(now / num[i]))
            div += 1

dfs(1, num[0])
print(max_n)
print(min_n)


