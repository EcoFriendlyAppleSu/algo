# 신규 아이디 추천
#
# def solution(id):
#     newlist = []
#     dot_index = []
#
#     id = id.lower()
#
#
#     for x in range(len(id)):
#         if id[x].isalpha() == True or id[x].isdigit() == True or id[x] == "-" or id[x] == "_" or id[x] == ".":
#             newlist.append(id[x])
#
#     for x in range(len(newlist)-1):
#         if newlist[x] == '.' and newlist[x+1] == '.':
#             dot_index.append(x)
#
#     for x in range(len(dot_index)-1,-1,-1):
#         newlist.pop(dot_index[x])
#
#     if len(newlist) == 0:
#         newlist.append('a')
#     elif len(newlist) != 0:
#         if newlist[0] == '.':
#             newlist.pop(0)
#             if len(newlist) == 0:
#                 newlist.append('a')
#         if newlist[len(newlist)-1] == '.':
#             newlist.pop(len(newlist)-1)
#
#
#     if len(newlist) >= 16:
#         newlist = newlist[:15]
#         if newlist[0] == '.':
#             newlist.pop(0)
#         if newlist[len(newlist)-1] == '.':
#             newlist.pop(len(newlist)-1)
#     elif len(newlist) <= 2:
#         temp = newlist[len(newlist)-1]
#         while len(newlist) < 3:
#             newlist.append(temp)
#
#     return "".join(newlist)

def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    answer = 'a' if answer == ' ' else answer

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))


    return answer

if __name__ == '__main__':
    newId = "...!@BaT#*..y.abcdefghijklm"
    print(solution(newId))
