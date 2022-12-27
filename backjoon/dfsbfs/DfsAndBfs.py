'''
문제 : 1260
@copyright : backjoon
'''
from collections import defaultdict
from collections import deque

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
        print("vertex = ", vertex)
        print("stack = ", stack)
    return visited

def bfs(graph, start):
    visited, queue = set(), deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


if __name__ == '__main__':
    node, edge, start = map(int, input().split())
    graph = defaultdict(set)

    for i in range(edge):
        init, end = map(int, input().split())
        graph[init].add(end)
        graph[end].add(init)
    print(dict(graph))
    print(dfs(graph, start))
    print(bfs(graph, start))
