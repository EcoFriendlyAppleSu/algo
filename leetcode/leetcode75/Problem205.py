# 205. Isomorphic Strings
from collections import Counter

# 내가 놓친 부분은 순서를 생각하지 않은 채 무작정 Count를 진행했다.
# 접근 방식은 좋았으나 이번 문제는 같은 개수 + 위치까지 맞아야 정답인 문제이다.
# dictionary의 활용법을 잘 알아두자, 틀렸지만 Count 사용과 lambda를 이용해 정렬하는 것도 알아두자
def solution(s, t):
    if len(s) != len(t):
        return False
    s = list(s)
    t = list(t)
    sStringCountElementsList = sorted(Counter(s).values(), key= lambda value: value)
    tStringCountElementsList = sorted(Counter(t).values(), key= lambda value: value)

    print(sStringCountElementsList)
    print(tStringCountElementsList)

    if sStringCountElementsList == tStringCountElementsList:
        for x, y in zip(s, t):
            if x == y:
                return False
            else:
                return True
    else:
        return False

def solution2(s, t):
    d1 = {}
    d2 = {}
    for i, val in enumerate(s):
        d1[val] = d1.get(val,[]) + [i]

    for i, val in enumerate(t):
        d2[val] = d2.get(val, []) + [i]

    return sorted(d1.values()) == sorted(d2.values())

def solution3(s, t):
    print(set(zip(s,t)))
    print(len(set(zip(s, t))))
    print(len(set(s)))
    print("set(s) is ", set(s))

    print(len(set(t)))
    print("set(t) is ", set(t))

    return len(set(zip(s,t))) == len(set(s)) == len(set(t))


if __name__ == '__main__':
    s = "bbbaaaba"
    t = "aaabbbba"
    # print(solution3(s,t))

    print(list(map(s.find, s)))


