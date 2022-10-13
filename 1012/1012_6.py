import heapq

n = int(input())
h = []

for _ in range(n) :
    data = int(input())
    heapq.heappush(h, data)


result = 0
while len(h) != 1 :
    i = heapq.heappop(h)
    j = heapq.heappop(h)
    sum_ij = i + j
    result += sum_ij
    heapq.heappush(h, sum_ij)

print(result)