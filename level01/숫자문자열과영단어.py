from collections import defaultdict

def solution(s):
    board = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    boardDict = {}

    for index in range(len(board)):
        boardDict[board[index]] = str(index)

    for element in board:
        if element in s:
            s = str.replace(s,element, boardDict[element])
    return int(s)

if __name__ == '__main__':
    print(solution("one4seveneight"))
    print(solution("23four5six7"))
    print(solution("2three45sixseven"))
    print(solution("123"))


# O(n) -> 10 + 10 * (n * (1 + m2/m1)) -> 10n + 10*(m2/m1) + 10
# initialize data structures.     # max time O(n)
# while find next match:          # max time O(n*m1)
#     copy unchanged string.      # max time O(n)
#     copy replacement            # max time O((n/m1) * m2) + O(n)
# copy rest of the string         # max time O(n)
# 시간 복잡도 : O(n * (1 + m2/m1))
# 시간 복잡도에 대한 설명
# https://stackoverflow.com/questions/66163149/does-str-replace-have-a-time-complexity-on2