'''
최소 신장 트리를 구하는 방법 : 크루스칼 알고리즘
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
parent = [0] * (edge + 1)

values = []
result = 0
total = 0 # 가로등 전체 비용
for i in range(node):
    parent[i] = i

for _ in range(edge):
    a, b, cost = map(int, input().split())
    values.append((cost, a, b))

values.sort()  # 기본적으로 오름차순으로 유지됩니다.

for value in values:
    cost, a, b = value
    total += cost
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 모든 가로등을 다 켤 때 비용 - 최소 비용을 = 절약할 수 있는 최대 금액
print(total - result)

'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''
