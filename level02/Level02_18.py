# 예상 대진표
def solution(n,a,b):
    answer = 0
    if (n % 2) == 1 or a == b:
        return -1

    gameboard = [False for _ in range(n)]
    gameboard[a-1] = True
    gameboard[b-1] = True

    N = len(gameboard) // 2
    while True:
        for i in range(N):
            if (gameboard[2*i] is False) and  (gameboard[2 * i + 1] is False):
                gameboard[i] = False
            elif (gameboard[2*i] is True) and  (gameboard[2 * i + 1] is True):
                answer += 1
                return answer
            else:
                gameboard[i] = True
        answer += 1
        N //= 2

    return answer

def solutionAfterAnswer(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a,b = (a+1)//2,(b+1)//2
    return answer

if __name__ == '__main__':
    N = 8
    A = 4
    B = 7
    print(solution(N, A, B))
    print(solutionAfterAnswer(N,A, B))
