# i 번째 원소와 i + 1 번째 원소

def solution(mylist):
    answer = []
    for i in range(len(mylist) -1):
        answer.append(abs(mylist[i] - mylist[i+1]))
    return answer

# zip 함수 더 깊게 알아보기
# zip 함수에 서로 길이가 다른 리스트가 인자로 들어오는 경우에는
# 길이가 짧은 쪽 까지만 iteration이 이루어집니다.
def solutionUsingPythonZip(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]
    print(solution(mylist))
    print(solutionUsingPythonZip(mylist))