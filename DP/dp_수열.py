# 수열 2491번
n = int(input())
data = list(map(int, input().split()))

num = data[0]
dp = [[1,1] for _ in range(n)]

for i in range(1,n) :
    if num < data[i] :
        dp[i][0] = dp[i - 1][0] + 1
    elif num > data[i] :
        dp[i][1] = dp[i - 1][1] + 1
    else :
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = dp[i - 1][1] + 1
    num = data[i]

result = 0
for i in dp :
   a, b= i
   if result < a :
       result = a
   if result < b :
       result = b
#print(dp)
print(result)