# 문자열 압축

def solution(string):
    result = []

    if len(string) == 1: # 주어진 문자열의 길이가 1일 때,
        return 1 # return 1

    for i in range(1, (len(string)//2)+1): # 반복을 진행, 반복 시 절반을 넘을 수 없어 //2 + 1
        tempResult = '' # 매 반복 시 결과값 저장하는 tempResult
        count = 1 # 문자열이 연속으로 반복되는지 체크하는 숫자
        tempString = string[:i] # 다음 문자열과 연속되는지 보기 위한 변수

        for j in range(i, len(string), i): # i 부터 len(string)만큼 i 만큼 잘라서
            if tempString == string[j:i+j]: # 자른 문자열이 다음 문자열과 같을 때
                count += 1 # count + 1
            elif tempString != string[j:i+j]: # 자른 문자열이 다음 문자열과 다를 때
                if count != 1: # 만약 count가 1이 아니라면
                    # 기존 문자열 = 기존 문자열 + 반복 횟수 + 반복된 문자열
                    tempResult = tempResult + str(count) + tempString
                else: # 만약 count가 1이라면
                    # 기존 문자열 = 기존 문자열 + 반복된 문자열, 반복 횟수가 1일 경우 생략한다.
                    tempResult = tempResult + tempString
                tempString = string[j:j+i] # 다음으로 순회할 연속된 문자열을 저장
                count = 1 # count 초기화
        if count != 1: #
            tempResult = tempResult + str(count) + tempString
        else:
            tempResult = tempResult + tempString

        result.append(len(tempResult))
        print(tempResult)
    print(result)
    return min(result)


if __name__ == '__main__':
    string = "aabbaccc"
    print(solution(string))