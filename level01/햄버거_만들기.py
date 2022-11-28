'''
슬라이싱 말고 앞으로 나아가면서 값을 하나씩 핸들링 하는 것을 배우자sa
'''
def solution(ingredient):
    answer = 0
    burger = []
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1,2,3,1]:
            answer += 1
            for i in range(4):
                burger.pop()
    return answer

if __name__ == '__main__':
    print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
