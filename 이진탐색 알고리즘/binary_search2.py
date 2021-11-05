# bisect 라이브러리를 활용
# bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

from bisect import bisect_left, bisect_right

# array = [1, 2, 4, 4, 8]
# x = 4
#
# print(bisect_left(array, x))
# print(bisect_right(array, x))

# =============================================================
# 범위안의 해당하는 데이터의 개수를 구하는 방법
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 8, 9]

print(count_by_range(array, 4, 4))
