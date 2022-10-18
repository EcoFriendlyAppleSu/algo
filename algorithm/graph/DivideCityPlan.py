# 도시 분할 계획
# 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다.

# 집, 가중치
node, edge = map(int, input().split())

parent = [0] * (node + 1)
edges = []
result = 0

for i in range(1, node + 1):
    parent[i] = i

# a집에서 b집으로 가는 가중치가 c입니다.
for _ in range(edge):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))


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


edges.sort() # sort를 하면 항상 오름차순 기준입니다.
last = 0

for index in edges:
    cost, a, b = index
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost
        last = cost

# 결과에서 가장 큰 가중치를 제외하면 가장 싼 값에 두 공간을 나눌 수 있습니다.
print(result - last)

# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4