# 기본중의 기본
# 순열, 조합, 중복순열, 부분집합 ==> 재귀문제의 기본
# 완전탐색의 기본 토대를 쌓는 과정

n = int(input())
arr = list(map(int, input().split()))

visited = [0] * len(arr)
result = [0] * n


# ========================================
# 순열
def perm(lev):
    if lev == n:
        print(*result)
        return

    for i in range(len(arr)):
        if visited[i] == 1:
            continue
        result[lev] = arr[i]
        visited[i] = 1
        perm(lev + 1)
        visited[i] = 0

# perm(0)

# =========================================
# 중복 순열
def r_perm(lev):
    if lev == n:
        print(*result)
        return

    for i in range(len(arr)):
        result[lev] = arr[i]
        r_perm(lev + 1)

# r_perm(0)

# ===========================================
# 조합
def com(lev, start):
    if lev == n:
        print(*result)
        return

    for i in range(start, len(arr)):
        result[lev] = arr[i]
        com(lev + 1, i + 1)

# com(0, 0)

# ============================================
# 부분집합 ( O, X 선택하고 선택하지 않는 경우 재귀를 돌떄 응용할 수 있다.)
def subset(lev, ss):
    if lev == n:
        if not ss:
            return
        print(ss)
        return

    subset(lev + 1, ss) # 해당 원소를 선택하지 않는다
    subset(lev + 1, ss + [arr[lev]]) # 해당 원소를 선택한다.

# subset(0, [])

