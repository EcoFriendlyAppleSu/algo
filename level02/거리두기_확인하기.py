# from itertools import combinations
#
# def calManhattanDistance(one, two):
#     return abs(one[0] - two[0]) + abs(one[1] - two[1])
#
# def isSameRowOrColumn(one, two):
#     # same column or same row
#     if one[0] == two[0] or one[1] == two[1]:
#         return True
#     else:
#         return False
#
#
# def solution(places):
#     answer = []
#
#     for place in places:
#         pLocation = []
#         # get Person Location
#         for i in range(len(place)):
#             for j in range(len(place[i])):
#                 if place[i][j] == 'P':
#                     pLocation.append((i,j))
#         # 조합 구하고
#         combinPLocation = combinations(pLocation, 2)
#
#         # mantattan distance <= 2 인 P 좌표를 구합니다.
#         for element in combinPLocation:
#             eleOne, eleTwo = element
#             if calManhattanDistance(eleOne, eleTwo) > 2:
#                 continue
#             else:
#                 if isSameRowOrColumn(eleOne, eleTwo): # is True
#                     if eleOne[0] == eleTwo[0]: # same column
#                         if abs(eleOne[1] - eleTwo[1]) == 2:
#                             if place[eleOne[0]][eleOne[1] + 1] == 'O':
#                                 answer.append(0)
#                                 break
#                         else:
#                             continue
#                     elif eleOne[1] == eleTwo[1]:
#                         if abs(eleOne[0] - eleTwo[1]) == 2:
#                             if place[eleOne[0] + 1][eleOne[1]] == 'O':
#                                 answer.append(0)
#                                 break
#
#                 else: # different location
#                     if (eleOne[0] + 1) == eleTwo[0] and (eleOne[1] + 1) == eleTwo[1] : # 두번째 Person이 우측 아래
#                         if place[eleOne[0]][eleOne[1] + 1] == 'O' or place[eleOne[0] + 1][eleOne[1]] == 'O':
#                             answer.append(0)
#                             break
#
#                     else:
#                         if place[eleOne[0] + 1][eleOne[1]] == 'O' or place[eleOne[0]][eleOne[1] - 1] == 'O':
#                             answer.append(0)
#                             break
#         else:
#             answer.append(1)
#     return answer

from collections import deque

def check(place, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([x, y, 0])
    visited = set()
    visited.add(tuple([x, y]))
    while queue:
        a, b, c = queue.popleft()
        if c == 2:
            continue
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and nx <= len(place)-1 and ny >= 0 and ny <= len(place[0])-1:
                if tuple([nx, ny]) not in visited:
                    visited.add(tuple([nx, ny]))
                    if place[nx][ny] == 'P':
                        return False
                    if place[nx][ny] == 'X':
                        continue
                    queue.append([nx, ny, c+1])

    return True


def solution(places):
    answer = []

    for place in places:
        people = []
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P':
                    people.append([i, j])

        flag = True
        for x, y in people:
            if not check(place, x, y):
                flag = False
                break

        if flag:
            answer.append(1)
        else:
            answer.append(0)


    return answer


if __name__ == '__main__':
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
