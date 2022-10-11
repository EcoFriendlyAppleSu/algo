# 플로이드 워셜 알고리즘 최단거리

INF = int(1e9)

node = int(input())
edge = int(input())

graph = [[INF] * (node + 1) for _ in range(node +1)]

# 초기값 세팅
for a in range(1, node +1):
    for b in range(1, node + 1):
        if a == b:
            graph[a][b] = 0

# 각 노드 가중치 입력
for _ in range(edge):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, node + 1):
    for b in range(1, node + 1):
        if graph[a][b] == INF:
            print("INFINITY", end= ' ')
        else:
            print(graph[a][b], end= ' ')
    print()
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2