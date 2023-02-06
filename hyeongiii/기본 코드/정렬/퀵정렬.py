"""
퀵 정렬
: 기준을 설정한 다음 큰 수와 작은 수를 교환한 후, 리스트를 반으로 나누는 방식으로 동작한다.
1. 리스트에서 첫 번째 데이터를 피벗으로 설정한 뒤, 왼쪽에서부터 피벗보다 큰 데이터를 선택하고 오른쪽에서부터 피벗보다 작은 데이터를 선택한 뒤 두 데이터의 위치를 서로 변경한다.
2. 왼쪽에서부터 찾는 값과 오른쪽에서부터 찾는 값의 위치가 서로 엇갈리게 되면, '작은 데이터'와 '피벗'의 위치를 서로 변경한다.
3. 피벗을 기준으로 왼쪽에는 피벗보다 작은 데이터가 위치하고 오른쪽에는 피벗보다 큰 데이터가 위치한다. 이 과정을 분할 혹은 파티션 이라고 한다. (분할 완료)
4. 이후 분할된 왼쪽 리스트와 오른쪽 리스트를 1-3 과 동일한 방식으로 정렬한다.

- 시간 복잡도 : O(N logN)
- 데이터가 무작위로 입력되는 경우 퀵정렬은 빠르게 동작하나,  데이터가 이미 정렬되어 있는 경우에는 매우 느리게 동작한다.
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개일 경우, 종료
        return
    pivot = start # 피벗은 첫 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right >= start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= tail]    # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]    # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)