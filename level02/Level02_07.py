# 메뉴 리뉴얼
from itertools import combinations # 난수 생성
from collections import Counter #

def solution(orders, course):
    answer = []

    for num in course: # 코스요리 메뉴 개수
        ary = []
        for order in orders: # 주문 현황
            order = sorted(order)
            ary.extend(list(combinations(order, num)))

        count = Counter(ary) # Counter 객체 init dict type object, count elements
        print(count)
        if count != 0:
            if max(count.values()) >= 2: # 제일 많이 나온 값이 두 번 이상 시켜졌다면
                for key, value in count.items():
                    if value == max(count.values()):
                        answer.append("".join(key))

    return sorted(answer)

if __name__ == '__main__':
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    print(solution(orders, course))