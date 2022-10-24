'''병사 배치하기'''
n = int(input())
data = list(map(int,input().split()))
data.reverse()

dp = [1] * n
max_value = 1
for i in range(1, n) :
    for j in range(i) :
        if data[j] < data[i] :
            dp[i] = max(dp[i], dp[j]+1)
        # 시간 +됨
        # if max_value + 1 == dp[i] :
        #     max_value = max(dp[i], max_value)
        #     break
print(n - max(dp))