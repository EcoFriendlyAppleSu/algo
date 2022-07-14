# All type change
# 모든 맴버의 타입을 변경할 땐 map을 사용하자 어렵게 생각하지 말고
def solution(mylist):
    answer = []
    for i in mylist:
        answer.append((int)(i))
    return answer

def solutionLikePython(mylist):
    answer = list(map(int, mylist))
    return answer
if __name__ == '__main__':
    input = ['1', '100', '33']
    print(solution(input))
    print(solutionLikePython(input))
