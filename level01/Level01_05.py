# 키패드 누르기 // 좌표에 익숙해지기
def solution(numbers, hand):
    answer = ''

    leftSide = [1,4,7]
    rightSide = [3,6,9]

    dial = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    leftHandPosition = dial['*']
    rightHandPosition = dial['#']

    for i in numbers:
        currentPosition = dial[i] # 좌표 주입
        if i in leftSide:
            answer+='L'
            leftHandPosition = currentPosition
        elif i in rightSide:
            answer += 'R'
            rightHandPosition = currentPosition
        else:
            leftFromMiddleLength = 0
            rightFromMiddleLength = 0

            for a, b, c in zip(leftHandPosition, rightHandPosition, currentPosition):
                leftFromMiddleLength += abs(a-c)
                rightFromMiddleLength += abs(b-c)

            if leftFromMiddleLength < rightFromMiddleLength:
                answer += 'L'
                leftHandPosition = currentPosition
            elif leftFromMiddleLength > rightFromMiddleLength:
                answer += 'R'
                rightHandPosition = currentPosition
            else:
                if hand == 'left':
                    answer += 'L'
                    leftHandPosition = currentPosition
                else:
                    answer += 'R'
                    rightHandPosition = currentPosition

    return answer

if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers, hand))