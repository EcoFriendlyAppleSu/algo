# 특정 원소가 속한 집합을 찾습니다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기, 값이 작을 수록 위에 위치합니다.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


node, edge = map(int, input().split())
parent = [0] * (node + 1)

for i in range(1, node + 1):
    parent[i] = i

cycle = False

for i in range(edge):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)


if cycle:
    print("Cycle이 존재합니다.")
else:
    print("Cycle이 존재하지 않습니다.")