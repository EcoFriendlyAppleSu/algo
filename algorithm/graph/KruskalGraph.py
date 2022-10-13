# 신장 트리, 크루스칼 알고리즘
# 최소 비용으로 모든 노드를 포함하면서 사이클이 존재하지 않는 graph를 만들 때 사용합니다.

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


node, edge = map(int, input().split())
parent = [0] * (node + 1)

edges = []
result = 0

# 초기 root 값은 자신의 index값입니다.
for i in range(1, node + 1):
    parent[i] = i

for _ in range(edge):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for i in edges:
    cost, a, b = i
    # 사이클이 발생하지 않는 경우에 진행
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost
print(result)  # return 159

# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
