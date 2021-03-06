#=====================================================================================
# 특정한 수의 범위 안에 존재하는 모든 소수를 찾아야 할때 ---> 에라토스테네스의 체 알고리즘 사용

# 1. 2 부터 N 까지 모든 수를 나열 한다.
# 2. 처리하지 않은 가장 작은 자연수를 제외한다.(2의배수, 3의배수....)
# 3. 반복한다.

import math

n = 1000
# 처음엔 모든 수가 소수인것으로 초기화한다.
array = [True for i in range(n+1)]
# 2부터 n의 제곱근까지의 모든 수를 확인
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # 소수라면
        # i를 제외한 모든 배수 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')