'''
모든 노드가 같은 집합에 있다면 여행 가능한 것입니다.
'''
node, edge = map(int, input().split())
parent = [0] * (node + 1)
for i in range(1, node + 1):
    parent[i] = i


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

for i in range(node):
    data = list(map(int, input().split()))
    for j in range(node):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))

result = True

for i in range(edge - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i]):
        result = False

if result:
    print("YES")
else:
    print("NO")


'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''
