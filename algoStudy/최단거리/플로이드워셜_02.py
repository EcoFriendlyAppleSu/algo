'''
이코테 실전문제 : 플로이드
'''

INF = int(1e9)

city = int(input())
bus = int(input())
graph = [[INF] * (city + 1) for _ in range(city + 1)]

# 자기 자신한테 가는 버스는 존재하지 않음으로 0으로 초기화
for a in range(1, city + 1):
    for b in range(1, city + 1):
        if a == b:
            graph[a][b] = 0

# a 도시에서 b 도시로 이동하는 비용 c
for _ in range(bus):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, city + 1):
    for a in range(1, city + 1):
        for b in range(1, city + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, city + 1):
    for b in range(1, city + 1):
        if graph[a][b] == INF:
            print("infinity", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''