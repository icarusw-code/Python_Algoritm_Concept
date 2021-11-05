# 1.탐색 시작 노드를 스택에 삽입하고 방문처리한다.
# 2.스택 최상단 노드에 방문하지 않은 인접 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리
#   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3.더 이상 2번과정을 수행할 수 없을 때까지 반복
from typing import Counter


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
     [], #순서를 맞추기 위해 공백으로
     [2, 3, 8], #1에 연결된 노드
     [1, 7],
     [1, 4, 5],
     [3, 5],
     [3, 4],
     [7],
     [2, 6, 8],
     [1, 7]
 ]

visited = [False] * 9

dfs(graph, 1, visited)

########################################################
# 2차원 그래프를 DFS를 통해 순회하는 경우
# 얼음을 얼릴 수 있는 공간이 상,하,좌,우로 연결되어 있다고 표현
# 3x3얼음 틀이 있다고 가정
# 001
# 010
# 101
# '0'인 값이 상,하,좌,우로 연결되어 있는 노드를 묶으면 3묶음이 나온다.
# 1.특정 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 '0' 이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
# 2.방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문 할 수 있다.
# 1-2 과정을 모든 노드에 반복하면서 방문하지 않은 지점의 수를 센다.

# n x m 사이즈의 얼음틀
n, m = map(int, input().split())

# 2차원 리스트를 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드를 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대하여 음료 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result)
######################################################################
# 2차원 그래프를 DFS를 통해 순회하는 경우 (좌표로 표현)
# BOJ 2667 단지 번호 붙히기
n = int(input())
graph = []
num =[]

for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 1:
        global count 
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(x,y)
        return True
    return False

count = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(count)
            result += 1
            count = 0
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
    