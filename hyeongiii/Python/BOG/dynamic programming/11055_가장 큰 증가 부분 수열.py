import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().rstrip().split()))

dp = data.copy()

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))