# 서로소 집합 알고리즘

# 특정 원소가 속한 집합을 찾기, 경로를 압축시킬 수 있다.
def findParent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x: # 초기 설정 시, 각 노드의 루트 노드 값은 자신의 인덱스입니다.
        parent[x] = findParent(parent, parent[x])
    return parent[x]

# 다음과 같이 작성하면 find할 때 worst case가 될 수도 있다. 경로 압축을 사용하자.
# def findParent(parent, x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         return findParent(parent, parent[x])
#     return x

# 두 원소가 속한 집합을 합치기
def unionParent(parent, a,b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선을 입력
node, edge = map(int, input().split())
parent = [0] * (node + 1) # 부모 테이블 초기화

# 초기 부모 테이블 값은 자기 자신을 가리키게 만든다.
for i in range(1, node+1):
    parent[i] = i

# 두 노드를 연결하는 union을 사용. 아래와 같이 사용하게된다면 각 노드가 서로를 참조하게 될 수 있어 위험하다.
# for i in range(edge):
#     a, b = map(int, input().split())
#     unionParent(parent, a, b)

cycle = False # 서로 참조하는 것을 방지하기 위해 선언한 cycle flag

for i in range(edge):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if findParent(parent, a) == findParent(parent, b):
        cycle = True
        break
    else:
        unionParent(parent, a, b)

# 각 원소가 어디를 가리키는지 체크, 재귀를 통해 탐색
print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, node + 1):
    print(findParent(parent, i), end=' ')

print()

# 나뉘는 값을 모두 체크
print('부모 테이블 : ', end=' ')
for i in range(1, node + 1):
    print(parent[i], end=' ')

print()

if cycle:
    print("사이클이 존재합니다.")
else:
    print("사이클이 존재하지 않습니다.")

# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

