# 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# target 수를 입력 받고 리스트안에서 target 의 위치를 반환
# 구현의 시간이나 메모리를 줄여야 할때 이진탐색을 생각해본다.

# ======================================================================
# 이진탐색(재귀함수로 구현)
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 찾은 경우 중간점 인덱스를 반환
#     if array[mid] == target:
#         return mid
#     # 중간점보다 찾는값이 작으면 왼쪽을 확인
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     # 중간점보다 찾는값이 크면 오른쪽을 확인
#     elif array[mid] < target:
#         return binary_search(array, target, mid + 1, end)
#
# # 원소의 개수와, 찾고자하는 값 입력 받기
# n, target = list(map(int, input().split()))
#
# # 전체 원소 입력 받기
# array = list(map(int, input().split()))
#
# result = binary_search(array, target, 0, n - 1)
#
# # 이진 탐색 결과 수행
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result + 1)

# ======================================================================
# 이진탐색(반복문으로 구현)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return  mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)




