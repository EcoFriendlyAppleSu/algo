# 최단 경로를 구하는 방식 다익스트라
import sys
input = sys.stdin.readline # input() method 보다 더 빠른 방법
INF = int(1e9) # python에서 무한값을 입력하는 방법

# Node 개수, 간선의 개수 입력받기
node, edge = map(int, input().split())
startNode = int(input()) # 시작 노드 번호 입력

# graph를 node + 1 로 설정한 이유는 1부터 시작하기 위함
graph = [[] for i in range(node+1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 생성
visited = [False] * (node + 1)

# 시작 node를 기준으로 최단거리를 갖고 있는 distance 리스트 생성
distance = [INF] * (node + 1)

# 모든 간선 정보 입력
for _ in range(edge):
    a,b,c = map(int, input().split()) # a node에서 b node로 가는 비용이 c라는 의미
    graph[a].append((b,c)) # node index a에 [(b,c)]가 담겨있는 형태입니다

print(graph)
# 방문하지 않은 노드 중에서 가중치. 즉, 최단 거리가 짧은 노드의 번호를 반환하는 메서드
def getSmallestNode():
    minValue = INF
    index = 0
    # 순차 조회를 통해 구함
    for i in range(1, node + 1):
        # 만약 방문하지 않고 거리가 minValue보다 작다면
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            index = 1
    return index

# dijkstra method
def dijkstra(start):
    distance[start] = 0 # 처음 시작점은 자기 자신이 시작점이므로 가중치가 0이다.
    visited[start] = True # 처음 node 방문처리
    for j in graph[start]: # 시작 node에 연결된 node 순회
        distance[j[0]] = j[1] # ??

    # 시작 노드를 제외한 전체 node -1 번 반복
    for i in range(node -1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = getSmallestNode()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(startNode)

for i in range(1, node + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2