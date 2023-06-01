'''퇴사'''
n = int(input())
t = []
p = []

for _ in range(n) :
    i, j = map(int,input().split())
    t.append(i)
    p.append(j)

max_value = 0
dp = [0] * (n+1)
for i in range(n-1,-1,-1) :
    time = i + t[i]
    if time <= n :
        # dp[i] = max(p[i]+dp[time], dp[i+1])
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else :
        # dp[i] = dp[i+1]
        dp[i] = max_value

# print(dp[0])
print(max_value)
print(dp)
