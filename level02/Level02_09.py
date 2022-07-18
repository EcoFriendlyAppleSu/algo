# 뉴스 클러스터링
from itertools import combinations

def intersectionString(str1, str2): # 다중 교집합
    str1Temp = str1.copy() # 교집합 한 번 제거용도
    result = str1.copy()

    for i in str2:
        if i not in str1Temp:
            result.append(i)
        else:
            str1Temp.remove(i)
    return result


def unionString(str1, str2):
    result = []
    str1Temp = str1.copy()

    for i in str2:
        if i in str1Temp:
            str1Temp.remove(i)
            result.append(i)

    return result


def jarcard(unionStr, intersectionStr):
    if len(unionStr) == 0 and len(intersectionStr) == 0:
        return 1
    else:
        return len(unionStr) / len(intersectionStr)

def gettingDivideAry(strings):
    result = []
    for i in range(len(strings) - 1):
        if strings[i: i+2].isalpha() == True:
            result.append(strings[i: i+2])
    return result

def solution(str1, str2):
    answer = 0

    str1Member = gettingDivideAry(str1)
    str2Member = gettingDivideAry(str2)

    intersectionStr = intersectionString(str1Member, str2Member)
    unionStr = unionString(str1Member, str2Member)

    answer = 65536 * (jarcard(unionStr, intersectionStr))

    return round(answer)

if __name__ == '__main__':
    str1 = "E=M*C^2"
    str2 = "e=m*c^2"

    # 대소문자 상관 없음으로
    str1 = str1.upper()
    str2 = str2.upper()

    print(solution(str1, str2))