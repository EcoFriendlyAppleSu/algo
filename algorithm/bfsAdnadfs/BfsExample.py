'''
BFS 기본 문제
BFS는 queue를 사용합니다.
'''
from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9


def bfs(graph, start, visited):
    # 큐를 생성하고 첫번째 원소를 넣는다
    queue = deque([start])
    # 방문 처리해주고
    visited[start] = True

    # queue가 빌 때까지 반복한다.
    while queue:
        # 큐에서 하나의 원소를 뽑는다.
        node = queue.popleft()
        # 해당 원소를 출력한다.
        print(node, end=' ')

        # 해당 노드에 연결된 노드들을 살펴본다.
        for i in graph[node]:
            # 만약 방문하지 않은 노드라면
            if not visited[i]:
                # queue에 집어넣고
                queue.append(i)
                # 방문처리한다.
                visited[i] = True


bfs(graph, 1, visited)
