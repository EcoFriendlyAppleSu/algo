# 음양 더하기

def solution(absolutes, signs):
    answer = 0
    gatherAbsSign = list(zip(absolutes, signs))

    print(gatherAbsSign)

    for index in gatherAbsSign:
        if index[1] == False: # 음수일 때 계산
            answer = answer + (index[0] * (-1))
        elif index[1] == True: # 양수일 때 계산
            answer = answer + (index[0] * int(index[1]))

    return answer

if __name__ == '__main__':
    absolutes = [4,7,12]
    signs = [True,False,True]
    print(solution(absolutes, signs))


