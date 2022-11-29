# 26 카드 정렬하기
import heapq
n = int(input())
q = []
for _ in range(n) :
    heapq.heappush(q, int(input()))

result = 0
for _ in range(n-1) :
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    temp = a + b
    result += temp
    heapq.heappush(q, temp)

print(result)