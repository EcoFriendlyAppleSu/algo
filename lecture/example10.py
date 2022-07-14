# 조합
from itertools import permutations

# map 사용 시 type을 지정해주지 않으면 tuple type으로 결과를 출력한다.
def solution(mylist):
    answer = sorted(list(map(list, permutations(mylist))))
    return answer

def solutionNotUsingPythonAPI(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

if __name__ == '__main__':
    mylist = [2,1]
    # print(solution(mylist))
    print(solutionNotUsingPythonAPI(mylist))
