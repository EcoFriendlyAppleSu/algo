# Knapsack Greedy Practice
# 나눠 담는 알고리즘이야
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight # 가중치는 왜 들어있는거야

def knapsackMethod(items, capacity):
    answer = []
    items.sort(key= lambda x: x.ratio, reverse = True) # ratio 기준 내림차순 정렬
    usedCapacity = 0
    totalValue = 0

    for i in items:
        print(i.weight)
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else: # 무게가 capacity보다 클 때
            unusedWegiht = capacity - usedCapacity
            value = i.ratio * unusedWegiht
            usedCapacity += unusedWegiht
            totalValue += value

        if usedCapacity == capacity:
            break

    print("total value is ", totalValue)
    print(answer)


if __name__ == '__main__':
    item1 = Item(20, 100)
    item2 = Item(30, 120)
    item3 = Item(10, 60)
    cList = [item1, item2, item3]
    capacity = 70
    knapsackMethod(cList, capacity)


