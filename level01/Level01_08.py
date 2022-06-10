# 내적
# Lambdas are one line functions.
# They are also known as anonymous functions in some other languages.
# You might want to use lambdas when you don’t want to use a function twice in a program.
# They are just like normal functions and even behave like them.

# https://dev.to/thepythongeeks/python-lambda-function-258d : lambda 사용법

# def solution(a, b):
#     answer = list(map(lambda x,y:x*y ,a,b))
#     return sum(answer)
#
# if __name__ == '__main__':
#     a = [1,2,3,4]
#     b = [-3,-1,0,2]
#     print(solution(a,b))

iter1 = [1,3,5]
iter2 = [2,2,2]
result = sum(list(map(lambda x,y : x+y, iter1, iter2)))

print(result)
