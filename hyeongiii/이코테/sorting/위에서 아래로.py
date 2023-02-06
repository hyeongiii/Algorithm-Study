import sys
input = sys.stdin.readline

num = int(input())
data = []
for i in range(num):
    data.append(int(input()))

data.sort()

for i in data:
    print(i, end=" ")