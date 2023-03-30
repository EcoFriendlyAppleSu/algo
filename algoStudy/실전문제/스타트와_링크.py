'''
https://www.acmicpc.net/problem/14889
중복을 처리하지 못해 해결하지 못했습니다.
'''

import sys; input = sys.stdin.readline
from itertools import combinations

def get_answer():
    global answer
    for start_member in list(combinations(member_all, N//2)):
        start_total = link_total = 0
        link_member = list(set(member_all) - set(start_member))
        for i, j in list(combinations(start_member, 2)):
            start_total += s_all[i][j]
            start_total += s_all[j][i]
        for i, j in list(combinations(link_member, 2)):
            link_total += s_all[i][j]
            link_total += s_all[j][i]
        answer = min(answer, abs(start_total - link_total))

if __name__ == "__main__":
    N = int(input())
    s_all = [list(map(int, input().split())) for _ in range(N)]
    member_all = list(range(N))
    answer = int(1e9)
    get_answer()
    print(answer)

# n =  int(input())
# board = [[] for _ in range(n)]
# visit = [0] * n
#
# total_scores = []
# amount_of_players = n // 2

# for i in range(n):
#     board[i] = list(map(int, input().split()))
#
# def get_total_score(board, board_size):
#     temp = []
#     for i in range(1, board_size):
#         for j in range(i):
#             temp.append(board[j][i] + board[i][j])
#     return temp
#
# def get_combination(total_scores, combination_size):
#     result = []
#     if combination_size == 0:
#         return [[]]
#     if combination_size == 1:
#         result = [[i] for i in total_scores]
#         return result
#     for i in range(len(total_scores)):
#         element = total_scores[i]
#         c = get_combination(total_scores[i+1:], combination_size-1)
#         for each_result in c:
#             result.append([element]+each_result)
#     return result
#
# def get_minimum_result(two_scores_list):
#     temp = int(1e9)
#     for two_scores in two_scores_list:
#         start, link = two_scores
#         if temp > abs(start-link):
#             temp = abs(start-link)
#     return temp
# total_scores = get_total_score(board, n)
# combination_result = get_combination(total_scores, amount_of_players)


'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
'''