# 19 연산자 끼워 넣기
# from collections import deque
n = int(input())
data = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

max_n = -1e9
min_n = 1e9

# q = deque([data[0]])

def dfs(num, i) :
    global plus, minus, multi, div, max_n, min_n
    if i == n :
        max_n = max(max_n, num)
        min_n = min(min_n, num)
        # print(q, num)
        return
    else :
        if plus > 0 :
            plus -= 1
            # q.append(('+',num + data[i]))
            dfs(num + data[i], i+1)
            # q.pop()
            plus += 1
        if minus > 0:
            minus -= 1
            # q.append(('-',num - data[i]))
            dfs(num - data[i], i+1)
            # q.pop()
            minus += 1
        if multi > 0:
            multi -= 1
            # q.append(('*', num * data[i]))
            dfs(num * data[i], i+1)
            # q.pop()
            multi += 1
        if div > 0:
            div -= 1
            # q.append(('//', int(num / data[i])))
            dfs(int(num / data[i]), i+1)
            # q.pop()
            div += 1
dfs(data[0], 1)
print(max_n)
print(min_n)
