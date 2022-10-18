# 위상 정렬

from collections import deque

node, edge = map(int, input().split())
indegree = [0] * (node + 1)
graph = [[] for i in range(node + 1)]

# 간선을 차감하면서 진행해야하니 edge 만큼 loop 진행
for _ in range(edge):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1 # b node가 갖고 있는 것을 줄이면서 sort 진행되야함

def topologySort():
    result = []
    queue = deque()

    # 처음 초기화 시 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, node + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1을 빼기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=' ')
topologySort()

# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4


