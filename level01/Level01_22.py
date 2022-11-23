'''
문제 : 치킨 쿠폰
'''

def solution(chicken):
    answer = 0
    while chicken >= 10:
        div, mod = divmod(chicken, 10)
        answer += div
        chicken = div + mod
    return answer

if __name__ == '__main__':
    print(solution(1081))
