'''
풀지 못한 이유를 생각해 봅시다.
문제를 너무 어렵게 생각했나??
'''
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: [x[1], x[0]])
    print(targets)
    start, end = 0, 0

    for target in targets:
        if target[0] >= end: # 끝점값보다 시작 점이 크다면 end 점 값을 교체하고
            answer += 1
            end = target[1]

    return answer

if __name__ == '__main__':
    targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
    print(solution(targets))