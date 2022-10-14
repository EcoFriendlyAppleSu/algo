# H index 구하기
citations = [3, 0, 6, 1, 5]
hindex= -1

citations = sorted(citations, reverse=True)
result = 0
for i in range(len(citations)):
    if citations[i] <= i:
        result = i
        break
    result = len(citations)

print(result)