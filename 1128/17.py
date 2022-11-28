# 17 경쟁적 전염
import heapq
# deque도 가능 -> 리스트에 넣고 sort 후 deque에 넣기
n, k = map(int, input().split())
data = []
q = []
for i in range(n) :
    temp = list(map(int, input().split()))
    data.append(temp)
    for j in range(n):
        if temp[j] != 0 :
            heapq.heappush(q,(0,temp[j],i,j))

s, x, y = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
while q :
    time, num, i, j = heapq.heappop(q)
    if time == s : break
    for k in range(4) :
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= n : continue
        if data[nx][ny] == 0 :
            data[nx][ny] = num
            heapq.heappush(q, (time+1, num, nx, ny))

# for i in range(n) :
#     for j in range(n) :
#         print(data[i][j], end= " ")
#     print()
print(data[x-1][y-1])


