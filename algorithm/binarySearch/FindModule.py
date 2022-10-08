# 부품 찾기

# 갖고 있는 부품의 종류
N = int(input())
NList = list(map(int, input().split()))

# 사용자가 원하는 부품의 종류
M = int(input())
MList = list(map(int, input().split()))

componentList = sorted(NList)

def binarySearch(componentList, component, start, end):

    if start > end:
        return None

    mid = (start + end) // 2

    if componentList[mid] == component:
        return True
    elif componentList[mid] < component:
        return binarySearch(componentList, component, mid + 1, end)
    elif componentList[mid] > component:
        return binarySearch(componentList, component, start, mid - 1)

result = []
for component in MList: # 각 부품마다 체크

    if binarySearch(componentList, component, 0, len(NList)-1) == None:
        result.append("no")
    else:
        result.append("yes")

print(result)

# 5
# 8 3 7 9 2
# 3
# 5 7 9