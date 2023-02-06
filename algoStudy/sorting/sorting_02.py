'''
백준 문제 : 국영수
'''


# from collections import defaultdict
# import sys
# n = int(sys.stdin.readline())
# students = defaultdict(list)
# for i in range(n):
#     name, guk, eng, math = list(map(str, sys.stdin.readline().split()))
#     students[name].append(int(guk))
#     students[name].append(int(eng))
#     students[name].append(int(math))
#
# students = students.items()
# gukSorted = sorted(students, key=lambda x: x[1][0], reverse=True)
# print(gukSorted)
#
# sorted(gukSorted, key=lambda a, b: a[1][0])

import sys

N = int(sys.stdin.readline())
table = [list(sys.stdin.readline().split()) for _ in range(N)]

table.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in table:
    sys.stdout.write(str(student[0]) + "\n")

'''
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''