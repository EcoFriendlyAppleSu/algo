'''
플로이드 워셜 모양을 하고 있는 다익스트라 문제
'''

# import heapq
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
# # time = int(input)
# nSize = int(input())
# weightMap = [list(map(int, input().split())) for i in range(nSize)]
# startPoint = (0,0)
# endPoint = [(nSize-1, nSize-1)]
#
# graph = [[] for _ in range(nSize)]
# print(weightMap)
# for i in range(nSize): # 0 1 2
#     for j in range(nSize): # 0 1 2
#         graph[i].append((j, weightMap[i][j]))
#
# print(graph)
#
# def dijkstra(start):
#     queue = []
#     x, y = start
#     startWeight = weightMap[x][y]
#     heapq.heappush(queue, (startWeight, start))
#
#     while queue:
#         currenctCost, currentNode = heapq.heappop(queue)
#         xCurrentNodePosition, yCurrentNodePosition = currentNode
#
#         if weightMap[xCurrentNodePosition][yCurrentNodePosition] < currenctCost:
#             continue
#
#         for i in range(len(graph[xCurrentNodePosition])): # y노드로가는 가중치 c
#             cost = currenctCost + graph[xCurrentNodePosition][i][1]
#
#             if cost < weightMap[i][graph[xCurrentNodePosition][i][0]]:
#                 weightMap[i][graph[xCurrentNodePosition][i][0]] = cost
#                 heapq.heappush(queue, (cost, graph[i][graph[xCurrentNodePosition][i][0]]))
#
# dijkstra(startPoint)
#
# print(weightMap)

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

nSize = int(input())
graph = []
for i in range(nSize):
    graph.append(list(map(int, input().split())))

distance = [[INF] * nSize for _ in range(nSize)]

x, y = 0, 0
queue = [(graph[x][y], x, y)]
distance[x][y] = graph[x][y] # 시작 비용 초기화

while queue:
    currenctCost, x, y = heapq.heappop(queue)

    if distance[x][y] < currenctCost:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= nSize or ny < 0 or ny >= nSize:
            continue
        cost = currenctCost + graph[nx][ny]

        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(queue, (cost, nx, ny))

print(distance[nSize-1][nSize-1])


'''
3
5 5 4
3 9 1
3 2 7
'''
