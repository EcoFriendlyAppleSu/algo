# 다익스트라 힙 사용
import heapq # priority queue. 최대값과 최소값을 사용할 때 유리하다.
import sys
input = sys.stdin.readline
INF = int(1e9)

node, edge = map(int, input().split())
start = int(input())

graph = [[] for i in range(node + 1)]
distance = [INF] * (node + 1)

for _ in range(edge):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # queue가 빌 때까지 진행 -> 순차 탐색과 다르게 매번 최소 index를 찾는 수고로움이 없다.
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, node + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
