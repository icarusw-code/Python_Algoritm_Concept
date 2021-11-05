# 가장 짧은 경로를 찾는 알고리즘
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙을 이용
# 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙 사용

import heapq
import sys

INF = sys.maxsize # 최대 값을 사용

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력 받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담기위해 링크드 리스트 만들기
graph =[[] for i in range(n+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단 거리는  0으로 설정, 큐에 삽입
    # 가중치 순으로 heapq 사용을 위해 가중치를 앞에 둔다
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 가중치가 높아서 큐에 남아 있던 놈들은 이미 최소값으로 최신화 했으므로 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 입접한 노드들을 확인
        # i[0] 연결되는 다음 노드 / i[1] cost
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드를 이동하는 거리가 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

##################################################################################
################################경로 출력 ########################################

import heapq
import sys

INF = sys.maxsize # 최대 값을 사용

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력 받기
start, end = map(int, input().split()) # <<<<<<<<<<=================== 추가 

# 각 노드에 연결되어 있는 노드에 대한 정보를 담기위해 링크드 리스트 만들기
graph =[[] for i in range(n+1)]
trace = [] * (n+1) # <<<<<<<<<<=================== 추가 

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단 거리는  0으로 설정, 큐에 삽입
    # 가중치 순으로 heapq 사용을 위해 가중치를 앞에 둔다
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 가중치가 높아서 큐에 남아 있던 놈들은 이미 최소값으로 최신화 했으므로 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 입접한 노드들을 확인
        # i[0] 연결되는 다음 노드 / i[1] cost
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드를 이동하는 거리가 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                trace[i[0]] = now # <<<<<<<<<<=================== 추가 trace[다음노드] = 현재노드
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])