######################################################################
# 정렬되어 있는 리스트에서 탐색 범위를 좁혀가며 데이터를 탐색하는 방법
# 원소의개수, 찾고자하는 값
# 전체 원소 입력 받기

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    # 찾은 경우 중간점 인텍스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    
# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0 , n-1) #인덱스 번호 이므로 (0 ~ n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(str(result+1) + '번째 수 입니다.')


######################################################################
# # bisect 를 이용한 간단한 방법
# bisect_left: 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
# bisect_right: 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a,x)) # 2 
print(bisect_right(a,x)) # 4

######################################################################

# 값이 특정 범위에 속하는 데이터 구하기
from bisect import bisect_right, bisect_left

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(array, 4, 4)) # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(array, -1, 3)) # 6