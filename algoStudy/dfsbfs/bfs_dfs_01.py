'''
백준 문제 1260
'''

from collections import deque
from collections import defaultdict

def dfs(graph, visited,start):
    visited[start] = True
    print(start, end= ' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)
    return None

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        pop = queue.popleft()
        print(pop, end= ' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return None

if __name__ == '__main__':
    node, edge, start = map(int ,input().split())
    graph = defaultdict(list)
    dfsVisited = [False] * (node + 1)
    bfsVisited = [False] * (node + 1)

    # 인접 리스트 생성
    for i in range(edge):
        preNode, postNode = map(int, input().split())
        graph[preNode].append(postNode)
        graph[postNode].append(preNode)

    # value sorting
    graph = sorted(graph.items(), key=lambda x:x[1])
    graph = dict(graph)

    dfs(graph, dfsVisited, start)
    print()
    bfs(graph, bfsVisited, start)


'''
<<INPUT>>
4 5 1
1 2
1 3
1 4
2 4
3 4
'''