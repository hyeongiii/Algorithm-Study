import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1])))

array = sorted(data, key=lambda student:student[1])

for student in array:
    print(student[0], end=" ")