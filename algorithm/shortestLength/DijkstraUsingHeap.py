# 다익스트라 힙 사용
import heapq # priority queue. 최대값과 최소값을 사용할 때 유리하다.
import sys

# sys를 통해 입력
input = sys.stdin.readline
# 방문하지 않은 공간에선 무한값을 입력
INF = int(1e9)

# 노드와 간선 입력
node, edge = map(int, input().split())
# 시작 노드 입력
start = int(input())

# 순회 그래프 생성
graph = [[] for _ in range(edge)]
# 최소 거리는 아직 알지 못하기에 처음 시작을 제외한 나머지 모든 노드를 무한으로 초기화 node + 1로 초기화하는 이유는 1부터 시작하기 위함
distance = [INF] * (node + 1)

# a번 노드에서 b노드로 가는 비용이 c라는 의미
for _ in range(edge):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

print(graph)
# heapq에 들어가는 것과 graph에 들어가는 값이 다르다.
# heapq = (queueList, (cost, node))
# graph = (node, cost)
def dijkstra(start):
    # heapq에 들어갈 queue list
    queue = []
    # heapify가 정용될 list와 시작점 입력
    # heap이 적용된 queue에 처음 값 (cost, node)를 삽입
    heapq.heappush(queue, (0, start))
    # 시작 노드의 길이는 0
    distance[start] = 0

    # queue가 빌 때까지 진행 -> 순차 탐색과 다르게 매번 최소 index를 찾는 수고로움이 없다.
    while queue:
        # 현재 존재하는 heap의 값을 꺼낸다. 최소힙이기 때문에 .
        dist, cost = heapq.heappop(queue)

        # 만약 꺼낸 거리가 현재 거리보다 크다면
        if distance[cost] < dist:
            # continue
            continue
        # 그렇지 않다면 현재 노드와 연결된 곳을 순회
        for i in graph[cost]:
            # graph에서는 (node, 비용)인데..
            # 현재의 거리값 + (비용, 노드) 중 비용을 cost에 임의 저장
            cost = dist + i[1]
            # 만약 해당 비용이 현재의 노드의 비용보다 작다면
            if cost < distance[i[0]]:
                # 현재의 노드 비용은 대체되고
                distance[i[0]] = cost
                # 그 값의 가중치와 노드가 heap에 등록된다.
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)
for i in range(1, node + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
