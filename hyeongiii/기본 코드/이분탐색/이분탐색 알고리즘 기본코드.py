# 비재귀적 이분 탐색의 파이썬 코드 (반복문)
def binary_search(arr, val):
    start, end = 0, arr.len() - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            end = mid - 1
        else:
            start = mid + 1

    return None


# 재귀 함수로 구현한 이진 탐색 소스 코드 (arr은 오름차순으로 정렬된 리스트)
def binary_search(arr, target, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    # 찾은 경우 중간점 인덱스 반환
    if arr[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우, 왼쪽 확인
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽 확인
    else:
        return binary_search(arr, target, mid + 1, high)