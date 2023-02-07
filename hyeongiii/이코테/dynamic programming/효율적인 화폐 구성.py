import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

# 한 번 계산된 결과를 저장하기 위해 DP 테이블 초기화
dp = [10001] * (m + 1)
dp[0] = 0

# DP 진행 (보텀업)
for i in range(n):
    for j in range(data[i], m + 1):    # 화폐 단위(최소 금액) 부터 m까지 해당 화폐 단위를 사용하여 화폐를 구성할 수 있는지 확인
        if dp[j - data[i]] != 10001:    # (j - data[i]) 을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j - data[i]] + 1, dp[j])

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
