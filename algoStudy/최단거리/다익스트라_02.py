'''
개선된 다익스트라
'''

import heapq
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
    queue = []
    heapq.heappush(queue, (0, start)) # 거리 0, 노드 start
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist: # 처리된 노드가 거리가 작을 때 continue
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

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