import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [0] * n
dp[0] = data[0]
dp[1] = max(data[0], data[1])
dp[2] = data[0] + data[2]

for i in range(3, n):
    dp[i] = max(dp[i - 2] + data[i], dp[i - 1])

print(dp[n - 1])