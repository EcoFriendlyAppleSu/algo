'''
order = sorted(order) # str to list each element
문제를 잘 앍자, Counter library는 Dictionary type으로 숫자를 카운트한다.
'''
# 메뉴 리뉴얼
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for num in course: # 코스요리 메뉴 개수
        ary = []
        for order in orders: # 주문 현황
            order = sorted(order) # str to list each element
            ary.extend(list(combinations(order, num))) # 각 order를 배열에 추가

        count = Counter(ary) # 원소 count
        if count is True:
            if max(count.values()) >= 2:
                for key, value in count.items():
                    if value == max(count.values()):
                        answer.append("".join(key))

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
