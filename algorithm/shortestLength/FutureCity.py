# 미래 도시
INF = int(1e9)

Node, Edge = map(int, input().split())
graph = [[INF] * (Node + 1) for _ in range(Node + 1)]

# 자기 자신에게 가는 길을 0입니다.
for i in range(1, Node + 1):
    for j in range(1, Node + 1):
        if i == j:
            graph[i][j] = 0

# graph 간선 연결 각 Node의 거리는 1입니다.
for _ in range(Edge):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 중간에 들리는 Temp, 목적지 Dest
# start to temp + dest to temp => start to destination
Temp, Dest = map(int, input().split())

for i in range(1, Node + 1):
    for j in range(1, Node + 1):
        for k in range(1, Node + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

distance = graph[1][Dest] + graph[Dest][Temp]

if distance >= INF:
    print("-1")
else:
    print(distance)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
