'''
엣지케이스가 해결되지 않아 해결 못함
'''
def calculate_spot(r2_minus_one, r2):
    result = 0
    spots = set()

    value = r2_minus_one
    minus_value = (-1) * r2_minus_one

    for i in range(minus_value, value +1):
        spots.add((value, i))
        spots.add((i, value))
        spots.add((minus_value, i))
        spots.add((i, minus_value))

    r2_pow = (r2 ** 2)

    for spot in spots:
        x, y = spot
        spot_value = (x ** 2) + (y ** 2)
        if r2_pow < spot_value:
            continue
        result += 1

    return result

def solution(r1, r2):
    answer = 0

    for i in range(r1, r2):
        temp = 0
        temp += (i * 2)
        temp = temp ** 2
        answer += temp
        if i == (r2 - 1):
            calculate_spot(i, r2)
    answer += 4
    return answer


import math


def solution2(r1, r2):
    inner_dot_num = 0
    for x in range(1, r2 + 1):
        y_max = math.floor(math.sqrt(r2 ** 2 - x ** 2)) # 안에 속하는 점의 개수
        y_min = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1 ** 2 - x ** 2)))
        inner_dot_num += y_max - y_min + 1

    return inner_dot_num * 4

if __name__ == '__main__':
    r1 = 2
    r2 = 4
    print(solution2(r1, r2))