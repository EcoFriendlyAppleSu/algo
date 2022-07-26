# Greedy

def printMaxActivities(activities):
    print(activities)
    activities.sort(key=lambda x: x[2])
    print(activities)
    i = 0
    firstA = activities[i][0]
    print(firstA)

    for j in range(len(activities)): # len(activities) = 6
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j


if __name__ == '__main__':
    activities = [["A1", 0, 6],
                  ["A2", 3, 4],
                  ["A3", 1, 2],
                  ["A4", 5, 8],
                  ["A5", 5, 7],
                  ["A6", 8, 9]]
    printMaxActivities(activities)