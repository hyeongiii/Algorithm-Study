import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

while start <= end:
    mid = (start + end) // 2
    sum = 0

    for i in data:
        if i > mid:
            sum += (i - mid)

    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
