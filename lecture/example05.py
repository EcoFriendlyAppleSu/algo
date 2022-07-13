# 알파벳 출력하기
import string

# string module엔 상수로 정의된 많은 것들이 존재한다.
def solution(number):
    temp = []
    if number == 1:
        # for i in range(65, 91):
        #     temp.append(chr(i))
        print(string.ascii_uppercase)
    else:
        # for i in range(97, 123):
        #     temp.append(chr(i))
        print(string.ascii_lowercase)

if __name__ == '__main__':
    number = int(input().strip())
    solution(number)