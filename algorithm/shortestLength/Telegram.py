# 전보
import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
# 도시, 통로, 시작점 입력
node, edge, start = map(int, input().split())

graph = [[] for i in range(node + 1)]
distance = [INF] * (node + 1)  # 0은 제외

for _ in range(edge):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(graph)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        # now == cost
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]  # graph에선 node, cost 순서입니다.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(start)
print(distance)

count = 0
maxDistance = 0
for d in distance:
    if d != INF:
        count += 1
        maxDistance = max(maxDistance, d)
print(count-1, maxDistance)

# infinity = 0
# result = 0
# for i in distance:
#     if i == INF:
#         infinity += 1
#     else:
#         result += i
#
# print(infinity, result)
# 3 2 1
# 1 2 4
# 1 3 2
