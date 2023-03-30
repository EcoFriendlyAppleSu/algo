def combination(arr, n):
    result = []
    if n == 0: # pick element가 없다면
        return [[]] # 빈 배열 반환
    if n == 1: # pick element number가 1일 때
        result = [[i] for i in arr] # 뽑는 경우의 수는 len(ary)입니다.
        return result
    for i in range(len(arr)):
        elem = arr[i] # 처음 element를 저장하고
        c = combination(arr[i+1:], n-1) # pick number를 하나 줄이고 다시 combination method를 수행합니다.
        for rest in c:
            result.append([elem]+rest)
    return result


def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    if n == 1:
        result = [[i] for i in arr]
        return result
    for i in range(len(arr)):
        elem = arr[i]
        p = permutation(arr[:i]+arr[i+1:], n-1)
        for rest in p:
            result.append([elem]+rest)
    return result


data = [1, 2, 3, 4, 5]
print(permutation(data, 2)) # 순열
print(combination(data, 2)) # 조합