# 왕실의 나이트

# NightPosition = list(map(str, input().split()))
# print(NightPosition[0], NightPosition[1])

dx = [0,0,-1,1]
dy = [-1,1,0,0]
positions = ['L', 'R', 'U', 'D']
moveCase = [
    ['L','L','U'],
    ['L','L','D'],
    ['R','R','U'],
    ['R','R','D'],
    ['U','U','L'],
    ['U','U','R'],
    ['D','D','L'],
    ['D','D','R']
]

def solution():

    inputPosition = list(input())
    X, Y = ord(inputPosition[0])-96, int(inputPosition[1]) # Setting Night Position
    tempX, tempY = X,Y
    print(X,Y)
    count = 0
    for case in moveCase: # Ex, ['L','L','U'] night 한 번의 총 움직임
        X, Y = tempX, tempY
        for move in case: # Ex, 'L' night 한 번의 움직임
            nightSingleMove = positions.index(move)
            X = X + dx[nightSingleMove]
            Y = Y + dy[nightSingleMove]
        if X < 1 or Y < 1 or X > 8 or Y > 8:
            continue
        else:
            count +=1

    return count

def solutionUsingSteps():
    inputData = input()
    row = int(inputData[1])
    column = int(ord(inputData[0]) - int(ord('a'))) + 1
    steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

    result = 0
    for step in steps:
        nextRow = row + step[0]
        nextColumn = column + step[1]

        if nextRow >= 1 and nextRow <= 8 and nextColumn >= 1 and nextColumn <= 8:
            result += 1

    return result
if __name__ == '__main__':
    print(solutionUsingSteps())
    # print(solution())