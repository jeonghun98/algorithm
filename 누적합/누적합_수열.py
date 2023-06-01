# 수열 2559번
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
result = []
result.append(sum(data[:k]))
for i in range(n-k) :
    result.append(result[i] - data[i] + data[k+i])
print(max(result))