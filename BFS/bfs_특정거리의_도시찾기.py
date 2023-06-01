from collections import deque
# 입력 시간 줄이기
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

grap = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b = map(int, input().split())
    grap[a].append(b)

k_l = [-1] * (n+1)
k_l[x] = 0

result = []
q = deque()
q.append(x)
while q :
    now = q.popleft()

    # 시간단축(제외 가능)
    if k_l[now] >= k :
        continue
    for next_n in grap[now]:
        if k_l[next_n] == -1:
            k_l[next_n] = k_l[now] + 1
            q.append(next_n)

check = False
for i in range(1,n+1) :
    if k_l[i] == k :
        print(i)
        check = True
if check == False :
    print(-1)