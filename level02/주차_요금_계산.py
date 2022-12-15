import math
from collections import defaultdict

def feeCalculator(fees, stackTime):
    defaultTime, defaultCharge, perTime, perCharge = fees
    result = 0
    print("stackTime = ", stackTime)
    # 누적 시간이 기본 시간보다 적다면
    if stackTime < defaultTime:
        return defaultCharge
    else:
        result += defaultCharge
        result += math.ceil((stackTime - defaultTime) / perTime) * perCharge
        return result


def timeGapCalculator(inTime, outTime):
    result = 0

    inHour, inMinute = inTime.split(":")
    inHour = int(inHour)
    inMinute = int(inMinute)

    outHour, outMinute = outTime.split(":")
    outHour = int(outHour)
    outMinute = int(outMinute)

    result += (outHour - inHour) * 60
    result += outMinute
    result -= inMinute

    return result


def solution(fees, records):

    answer = []
    totalTime = 0 # 각 차량의 누적 시간을 담는 변수
    carList = defaultdict(list)
    lastOutValue = ['23:59','OUT']

    # 입/출차를 순회하면서 defaultdictionary에 적재
    # 1000
    for record in records:
        time, carNumber, inOrOut = record.split(" ")
        carList[carNumber].append([time,inOrOut])

    # sorted 함수를 사용하게 되면 list(tuple)로 변경되어 추가로 dict를 사용하려면 dict(sortedSomething) 해줘야합니다.
    carList = dict(sorted(carList.items()))
    print("carList = ", carList)

    # 1000
    for car in carList:
        if len(carList[car]) % 2 != 0:
            carList[car].append(lastOutValue)
        print(carList[car])

    # 1000
    for car in carList:
        takeTime = 0
        # 500
        for i in range(0, len(carList[car]), 2):
            takeTime += timeGapCalculator(carList[car][i][0], carList[car][i+1][0])
        answer.append(feeCalculator(fees, takeTime))
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
