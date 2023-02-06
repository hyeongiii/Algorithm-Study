import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

# 내가 푼 풀이
for i in b:
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == i:
            print("yes", end=" ")
            break
        elif a[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    if start > end:
        print("no", end=" ")


# 책 풀이
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


for i in b:
    result = binary_search(a, i, 0, n - 1)
    if result is not None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
