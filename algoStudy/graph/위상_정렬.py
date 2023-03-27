'''
위상 정렬, 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있습니다.
방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것입니다.
'''

from collections import deque

node, edge = map(int, input().split())
indegree = [0] * (node + 1)
graph = [[] for i in range(node + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    queue = deque()

    # 진입 차수가 0이라면 queue에 넣습니다.
    for i in range(1, node + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''
