'''
이코테 실전문제 : 정확한 순위
전체에 대해서 현재 노드가 가리키는 곳이 있고 다른 노드에서 가리킴을 당하고 있다면 또한, 그 수가 node의 수와 같을 땐
모두의 성적을 보고 내 위치를 알 수 있다는 것을 이야기합니다.
'''

INF = 100

node, edge = map(int, input().split())
graph = [[INF] * (node + 1) for _ in range(node + 1)]

for a in range(1, node + 1):
    for b in range(1, node + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for index in graph:
    print(index)

result = 0

for i in range(1, node + 1):
    count = 0
    for j in range(1, node + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == node:
        result += 1
print(result)

'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
