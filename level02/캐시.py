'''

'''

from collections import deque


def solution2(cacheSize, cities):
    answer = 0
    cache = deque()

    # 100,000
    for city in cities:
        city = str(city).lower()

        if cacheSize == 0:
            answer += 5
            continue

        # 900
        if city in cache:
            cache.remove(city)
            cache.appendleft(city)
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.appendleft(city)
                answer += 5
            else:
                cache.pop()
                cache.appendleft(city)
                answer += 5

    return answer


# def solution(cacheSize, cities):
# answer = 0
# hit = 0
# miss = 0
# temp = deque()
#
# # 소문자로 변경
# for i in range(len(cities)):
#     cities[i] = cities[i].lower()
# queueCity = deque(cities)
#
# while queueCity:
#     currentCity = queueCity.popleft() # 왼쪽에서 하나를 꺼냅니다.
#
#     if cacheSize == 0:
#         miss += 1
#         temp.append(currentCity)
#         continue
#     else:
#         if len(temp) == 0:
#             temp.append(currentCity)
#             miss += 1
#         else: # 캐시가 비어있지 않을 때
#             print("current city = ", currentCity)
#             print("temp = ", list(temp))
#             if currentCity in temp: # 캐시에 있는 도시라면
#                 hit += 1 # 맞췄으니 hit 추가하고
#                 temp[0], temp[temp.index(currentCity)] = temp[temp.index(currentCity)], temp[0] # swap
#             elif currentCity not in temp: # 캐시에 있지 않은 도시라면
#                 temp.pop() # 캐시의 오른쪽 값을 빼고
#                 miss += 1 # 맞추지 못했으니 miss 추가하고
#                 temp.appendleft(currentCity) # 왼쪽으로 한 값을 추가합니다.
# print(answer, miss)
# answer = hit + (5 * miss)
# return answer


if __name__ == '__main__':
    # print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    # print(solution2(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    # print(solution2(1, ["a", "b", "b", "B", "a"]))
    print(solution2(2, ["a", "a", "a", "b", "b", "b", "c", "c", "c"] ))

    # print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    # print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
