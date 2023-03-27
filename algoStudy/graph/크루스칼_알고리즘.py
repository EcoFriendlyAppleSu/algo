'''
최단 신장 트리의 구현의 한 종류인 크루스칼 알고리즘 구현입니다.
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


node, edge = map(int, input().split())
parent = [0] * (node + 1)
edges = []
result = 0

for i in range(1, node + 1):
    parent[i] = i

for _ in range(edge):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정합니다.

edges.sort() # python은 기본적으로 처음 원소를 기준으로 정렬합니다.

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''
