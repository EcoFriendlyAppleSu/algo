'''
문제 : 택배 상자
while 반복문을 바라볼 때 while 안에 있는 조건식이 if라는 것을 잊지 말자
'''

def solution(order):

    stack = []
    i = 1
    now = 0

    while i != len(order) + 1:
        stack.append(i)
        while stack[-1] == order[now]:
            now += 1
            stack.pop()

            if len(stack) == 0:
                break
        i += 1
    return now

order = [4,3,1,2,5]
print(solution(order))