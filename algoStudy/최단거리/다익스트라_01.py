import sys

input = sys.stdin.readline
INF = int(1e9)

node, edge = map(int, input().split()) # 노드와 간선을 줍니다.

start = int(input()) # 시작 지점을 입력

graph = [[] for i in range(node + 1)] # 노드 연결 그래프를 생성

visited = [False] * (node + 1) # 방문을 체크하는 리스트 생성
distance = [INF] * (node + 1) # 거리를 모두 MAX 값으로 설정

for _ in range(edge):
    a, b, c = map(int, input().split())  # a 노드에서 b 노드로 가는 비용이 c
    graph[a].append((b, c))

# print(graph) return [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환합니다.
def getSmallestNode():
    minValue = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, node + 1):
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0 # 시작 노드에 대해서 초기화
    visited[start] = True # 시작 노드 방문

    for j in graph[start]: # 각 노드와 연결되어 있는 부분의 요소를 추출
        distance[j[0]] = j[1] # a 노드에서 b 노드로 가는 길의 값이 c --> b == j[0], c == j[1]

    for i in range(node - 1): # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
        now = getSmallestNode() # 현재 가장 짧은 노드를 꺼내 방문 처리, node와 distance 그리고 visited가 전역변수로 선언되어 가능
        visited[now] = True # 방문 처리

        for j in graph[now]: # 현재 노드와 연결된 다른 노드를 확인
            cost = distance[now] + j[1] # 현재 놓여있는 노드 까지의 최단 거리와 연결된 노드의 가중치를 합한 cost를 구함
            if cost < distance[j[0]]: # 다른 노드 까지의 기존에 존재하는 최단 거리 값이 연산된 값보다 클 경우
                distance[j[0]] = cost # 해당 cost를 노드의 최단 거리로 교체


dijkstra(start)

for i in range(1, node + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''