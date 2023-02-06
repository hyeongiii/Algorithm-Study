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


# 책 풀이 : 이분 탐색
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



# 책 풀이: 계수 정렬
n = int(input())
array = [0] * (n + 1)

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")



# 책 풀이: 집합 자료형 이용
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")