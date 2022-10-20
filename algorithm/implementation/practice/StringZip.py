# # 문자열 압축
#
# string = "aabbaccc"
# zipSize = 0
# result = []
# stringList = list(string)
#
# while zipSize <= len(stringList):
#     zipSize += 1
#     index = 0
#     if (len(stringList) % zipSize) != 0:
#         continue
#     else: # (len(stringList) % zipSize) == 0
#         while index < len(stringList):
#             if stringList[index : index + zipSize] == stringList[index + zipSize : index + (zipSize * 2)]:
#
