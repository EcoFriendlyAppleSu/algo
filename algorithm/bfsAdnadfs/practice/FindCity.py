'''
문제 : 특정 거리의 도시 찾기
모든 도로가 "1"이라는 조건 때문에 BFS를 사용할 수 있다.
'''

from collections import deque

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())

# 0을 제외한 번호에서 시작합니다.
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()
    for node in graph[now]:
        if distance[node] == -1:
            distance[node] = distance[now] + 1
            queue.append(node)

check = False
for i in range(1, n + 1):
   if distance[i] == k:
       print([i])
       check = True

if check == False:
    print(-1)

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4