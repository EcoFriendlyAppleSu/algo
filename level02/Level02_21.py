'''
문제 : 주차 요금 계산
Dictionary Data Structure 사용에 익숙해져보자
'''

from math import ceil

def chargeCalculator(fees ,time):
    defaultTime, defaultMoney, defaultMin, defaultMoney = fees
    return defaultMoney + (time - defaultTime) / defaultMin * defaultMoney

def solution(fees, records):
    answer = []
    carDict = {}
    finalTime = 23 * 60 + 59
    temp = []
    for record in records:
        time, carNumber, degree = record.split(" ")
        timeStamp = time.split(":")
        time = str(60 * int(timeStamp[0]) + int(timeStamp[1]))

        temp.append([time, carNumber, degree])
    print(temp)
    temp = sorted(temp, key= lambda x:x[1])
    print(temp)
    for i in range(len(temp)):
        carDict[temp[i][1]] = 0
    print(carDict)
    for i in range(len(temp)-1):
        chargeTime = 0
        # 입차 출차가 같을 때
        if temp[i][1] == temp[i+1][1]:
            if temp[i][2] == "IN" and temp[i+1][2] == "OUT":
                chargeTime += int(temp[i+1][1]) - int(temp[i][1])
            elif temp[i][2] == "OUT" and temp[i+1][2] == "IN":
                continue
            else:
                chargeTime += finalTime - int(temp[i][2])
        else:
            continue
        chargeCalculator(fees, chargeTime)

    return answer

def toMinutes(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def otherSol(fees, records):
    recs = {}
    fee = {}

    for record in records:
        time, carNumber, IO = record.split(" ")
        if carNumber in recs:
            recs[carNumber].append([time, IO])
        else:
            recs[carNumber] = [[time, IO]]

    for rec in recs:
        total = 0
        payment = fees[1]

        if len(recs[rec]) % 2 != 0:
            recs[rec].append(["23:59", "OUT"])

        for state in recs[rec]:
            if state[1] == "IN":
                total -= toMinutes(state[0])
            else:
                total += toMinutes(state[0])
        if total > fees[0]:
            payment += ceil((total - fees[0]) / fees[2]) * fees[3]

        fee[rec] = payment
    print(fee)
    fee = sorted(fee.items())

    return [f for n, f in fee]


if __name__ == '__main__':
    # print(solution([180, 5000, 10, 600],
    #                ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
    #                 "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
    print(otherSol([180, 5000, 10, 600],
                   ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                    "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))