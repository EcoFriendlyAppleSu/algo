'''
enumerate 존재 기억하기
'''
def solution(s):
    marked = {} # dictionary
    answer = [] # answer
    for index, letter in enumerate(s):
        answer.append(index - marked[letter] if letter in marked else -1)
        marked[letter] = index
    print(answer)

solution("banana")
