import math
def getTwoLengthSizeAry(s):
    result = []

    # 1000
    for i in range(len(s)):
        temp = s[i:i+2]
        if str(temp).isalpha() == False:
            continue
        if len(temp) != 2:
            continue
        result.append(temp)
    return result

def solution(str1, str2):
    answer = 0
    intersaction = {}
    union = {}

    # 1000
    str1 = str(str1).lower()
    str2 = str(str2).lower()

    print(str1, str2)

    # 1000
    str1Ary = getTwoLengthSizeAry(str1)
    str2Ary = getTwoLengthSizeAry(str2)

    print("집합 A = ", str1Ary)
    print("집합 B = ", str2Ary)

    # 1000
    setStr1 = set(str1Ary)
    # 1000
    setStr2 = set(str2Ary)

    print("교집합 = ", setStr1 & setStr2)

    # 999
    for index in setStr1 & setStr2:
        count1 = str1Ary.count(index)
        count2 = str2Ary.count(index)
        if count1 >= count2:
            intersaction[index] = count2
        else:
            intersaction[index] = count1

    print("j 교집합 = ",intersaction)

    print("합집합 = ", setStr1 | setStr2)

    # 999 * 2 = 2000
    for index in setStr1 | setStr2:
        count1 = str1Ary.count(index)
        count2 = str2Ary.count(index)
        if count1 >= count2:
            union[index] = count1
        else:
            union[index] = count2

    print("j 합집합 = ", union)

    print("sum of intersaction = ", sum(intersaction.values()))
    print("sum of union = ", sum(union.values()))

    try:
        answer = float(sum(intersaction.values()) / sum(union.values()))
    except ZeroDivisionError:
        answer = 1


    return math.trunc(answer * 65536)

# print(solution("E=M*C^2", "e=m*c^2"))
# solution("FRANCE", "french")
solution("aa1+aa2", "AAAA12")
# solution({1,1,2,2,3},  {1, 2, 2, 4, 5})
