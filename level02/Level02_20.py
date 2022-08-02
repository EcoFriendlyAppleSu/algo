# 후보키
from collections import Counter
from itertools import combinations
from collections import defaultdict


def findKeys(relation):
    answer = []
    combinationUsingNumberArys = [i for i in range(len(relation[0]))]
    for i in range(1, len(relation[0]) + 1):
        answer.extend(list(combinations(combinationUsingNumberArys, i)))
    return answer


def findSuper(relation, keys):
    superKeys = []
    subRelation = []
    rSize = len(relation)
    for key in keys:
        subRelation.clear()
        for i in range(rSize):
            subRelation.append(tuple(relation[i][k] for k in range(rSize) if k in key))
        if len(set(subRelation)) == rSize:
            superKeys.append(key)
    return superKeys


def findCandidate(superKeys):
    candidateKeys = []
    cSize = len(superKeys)
    for i, sk in enumerate(superKeys):
        if sk is False:
            continue
        candidateKeys.append(sk)
        for c in range(i + 1, cSize):
            if superKeys[c] is False:
                continue
            current = set(list(sk))
            target = set(list(superKeys[c]))
            if current.issubset(target):
                superKeys[c] = False
    return candidateKeys




def solution(relation):
    allKeys = findKeys(relation)
    superKeys = findSuper(relation, allKeys)
    candidateKeys = findCandidate(superKeys)
    return len(candidateKeys)

if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))