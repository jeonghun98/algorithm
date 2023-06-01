# 06 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    if sum(food_times) <= k :
        return -1

    q = []
    for i,d in enumerate(food_times) :
        heapq.heappush(q, (d, i+1))

    length = len(food_times)
    sum_value = 0 # 직전까지 사용한 시간
    previous = 0 # 전 data
    while sum_value + length * (q[0][0] - previous) < k :
        d, i = heapq.heappop(q)
        sum_value += (d - previous) * length
        length -= 1
        previous = d

    result = sorted(q, key=lambda x: x[1])
    print(result[(k-sum_value) % length][1]) #남은 시간 % 남은 접시 개수





