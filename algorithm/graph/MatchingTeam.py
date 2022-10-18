# 팀 결성

N, M = map(int,input().split())

parent = [0] * (N + 1)
for i in range(0, N + 1):
    parent[i] = i

def find_parent(parent, X):
    if parent[X] != X:
        parent[X] = find_parent(parent, parent[X])
    return parent[X]

# 작은 값이 우선권을 갖는 union method
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) != find_parent(parent, b):
            print("yes")
        else:
            print("no")

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1