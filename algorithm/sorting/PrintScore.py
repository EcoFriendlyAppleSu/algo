# 학생 성적이 낮은 순서대로 출력하기

time = int(input())
students = []

for i in range(time):
    students.append(tuple(map(str, input().split())))

def setting(student):
    return int(student[1])

result = sorted(students, key=setting)
print(result)

for i in result:
    print(i[0], end=" ")