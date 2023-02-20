'''
백준 문제 : 1로 만들기
DP table 점화식 세우기 : 해당 문제에선 "연산을 하는 횟수의 최소값"입니다.
DP table에 index의 값은 만드는 숫자를 뜻합니다.
위 점화식 테이블을 이루기 위해 주어진 조건을 사용해 규칙을 찾습니다.
'''

def dp(number):
    dpList = [0] * (number + 1)
    dpList[0] = 0
    dpList[1] = 0
    for i in range(2, number+1):
        dpList[i] = dpList[i - 1] + 1

        if i % 2 == 0:
            dpList[i] = min(dpList[i], dpList[i // 2] + 1)
        if i % 3 == 0:
            dpList[i] = min(dpList[i], dpList[i // 3] + 1)
    print(dpList)
    return dpList[number]


if __name__ == '__main__':
    number = int(input())
    print(dp(number))
