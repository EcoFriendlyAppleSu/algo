import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

node, edge = map(int, input().split())
graph = [[] for _ in range(node + 1)]
distance = [INF] * (node + 1)

start = 1
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        currentCost, now = heapq.heappop(queue)
        if distance[now] < currentCost:
            continue
        for i in graph[now]:
            cost = currentCost + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(start)

maxNode = 0
maxDistance = 0
result = []

for i in range(1, node + 1):
    if maxDistance < distance[i]:
        maxNode = i
        maxDistance = distance[i]
        result = [maxNode]
    elif maxDistance == distance[i]:
        result.append(i)
print(maxNode, maxDistance, len(result))

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
