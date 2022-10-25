'''
DFS 기본 문제
DFS는 Stack 알고리즘을 사용합니다.
'''
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

def dfs(graph, v, visited):
    # 방문처리
    visited[v] = True
    # 들린 곳 출력
    print(v, end=' ')

    # 방문한 곳의 node와 연결된 곳들을 순회
    for i in graph[v]:
        # 방문하지 않은 곳이라면, if visited[i] == False
        if not visited[i]:
            # 재귀를 통해 dfs 진행
            dfs(graph, i, visited)

dfs(graph, 1, visited)
