'''
문제 : 1260
@copyright : backjoon
'''
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for element in graph[vertex]:
            if not visited[element]:
                queue.append(element)
                visited[element] = True


def dfs(graph, vertex, visited):
    visited[vertex] = True
    print(vertex, end=' ')
    for element in graph[vertex]:
        if not visited[element]:
            dfs(graph, element, visited)


if __name__ == '__main__':
    node, edge, start = map(int, input().split())
    graph = [[] for _ in range(node + 1)]
    for i in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print("graph = ", graph)
    for i in range(1, node + 1):
        graph[i].sort()
    print("graph = ", graph)

    visitedDFS = [False] * (node + 1)
    dfs(graph, start, visitedDFS)

    print()
    visitedBFS = [False] * (node + 1)
    bfs(graph, start, visitedBFS)

'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
