# Joy Stick // greedy
import string

def solution(name):
    index = 0
    answer = 0
    strAscii = string.ascii_uppercase
    print(strAscii)

    name = list(name)

    for i in name:
        print(strAscii.index(i))


    return answer

if __name__ == '__main__':
    name = "JAN"
    print(solution(name))