'''
개선된 다익스트라
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
node, edge = map(int, input().split())
start = int(input())
graph = [[] for _ in range(node + 1)]
distance = [INF] * (node + 1)

for _ in range(edge):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # a 노드에서 시작되어 b 노드로 갈 때, 가중치 c가 들어갑니다.

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # queue에 (가중치, 현재 노드)를 넣습니다.
    distance[start] = 0 # 처음 시작은 0이구요

    while queue: # queue가 종료될 때까지
        currentCost, currentNode = heapq.heappop(queue)

        # 현재의 가중치보다 기존에 존재한 가중치가 작다면 continue
        if distance[currentNode] < currentCost:
            continue
        for i in graph[currentNode]:
            cost = currentCost + i[1]

            if cost < distance[i[0]]: # 만약 현재 위치의 가중치보다 비용이 적게 든다면
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for i in range(1, node + 1):
    if distance[i] == INF:
        print("INFINITY")
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