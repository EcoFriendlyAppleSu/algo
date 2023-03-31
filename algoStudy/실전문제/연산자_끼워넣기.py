'''
https://www.acmicpc.net/problem/14888
모든 경우의 수를 구하다보니 시간 초과가 발생했습니다.
'''


def make_operator_flat(operators):
    operator_sequence = ['+', '-', '*', '/']
    result = []
    for index, operator in enumerate(operators):
        result.extend(operator_sequence[index] * operator)
    return result


def permutation_operators(operators, operators_size):
    result = []
    if operators_size == 0:
        return [[]]
    if operators_size == 1:
        result = [[i] for i in operators]
        return result
    for i in range(len(operators)):
        element = operators[i]
        p = permutation_operators(operators[:i] + operators[i + 1:], operators_size - 1)
        for rest in p:
            result.append([element] + rest)
    return result


def operator_calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if a < 0:
            a = a * (-1)
            temp = a // b
            return temp * (-1)
        return a // b


def run_job(operands, total_operators):
    result = []
    for each_operator_set in total_operators:  # [['+', '*'], ['*', '+']]
        temp = 0
        for index, each_operator in enumerate(each_operator_set):
            if index == 0:
                temp = operands[index]
            cal_result = operator_calculator(temp, operands[index + 1], each_operator)
            temp = cal_result
        result.append(temp)
    return result


if __name__ == '__main__':
    # "['-', '/', '+', '+', '*'] "
    n = int(input())
    operands = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    operators = make_operator_flat(operators)
    total_operators = permutation_operators(operators, len(operators))
    result = run_job(operands, total_operators)
    print(min(result))
    print(max(result))

'''
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maxValue = -1e9
minValue = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maxValue, minValue
    if depth == N:
        maxValue = max(total, maxValue)
        minValue = min(total, minValue)
        return

    if plus:  # plus is not empty
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maxValue)
print(minValue)
'''

'''
3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
'''
