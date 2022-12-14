'''
인덱스를 갖고 값을 핸들링할 상황이 생긴다면
천천히 어떤 방식으로 인덱스를 이용할 것인지 생각해보자
또한 변경 지점을 유심히 봐야할 것 같습니다.
'''
import string

def solution(msg):
    answer = []
    summaryDictionary = {}

    alpha = string.ascii_uppercase
    index = 1

    for i in alpha:
        summaryDictionary[i] = index
        index += 1
    print("basic summaryDictionary = ", summaryDictionary)

    msg = list(msg) # 주어진 문자를 리스트로 만듭니다.
    check = '' # 딕셔너리에 포함되는 문자열을 저장하는 check 변수
    current = 0 # 시작하는 인덱스
    while current < len(msg):
        check += msg[current]
        if check in summaryDictionary:
            current += 1
        else:
            summaryDictionary[check] = len(summaryDictionary) + 1
            answer.append(summaryDictionary[check[:-1]])
            check = ''
    answer.append(summaryDictionary[check])
    return answer


print(solution("KAKAO"))