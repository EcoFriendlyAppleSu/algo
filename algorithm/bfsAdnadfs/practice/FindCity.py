'''
문제 : 특정 거리의 도시 찾기
모든 도로가 "1"이라는 조건 때문에 BFS를 사용할 수 있다.
'''

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # graph 생성

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)  # 거리 가중치를 저장하는 distance list
distance[x] = 0

queue = deque([x])

while queue:
    now = queue.popleft()
    for nextNode in graph[now]:
        if distance[nextNode] == -1:  # 방문하지 않은 곳일 때
            distance[nextNode] = distance[now] + 1
            queue.append(nextNode)

check = False
# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
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
