__author__ = 'suma'

from collections import defaultdict
import operator
import sys


def main():
    topicData = extractData()
    vocabDictionary = {}
    oneItemSet, transactionSet = generatetOneItemSetCandidates(topicData)      # C1
    prunedOneItemSet = calculateMinimumSupport(oneItemSet, transactionSet)     # L1

    frequentSet = prunedOneItemSet   # L1 frequent items
    k = 2
    while frequentSet != set([]):
        candidateSet = set([i.union(j) for i in frequentSet for j in frequentSet if len(i.union(j)) == k])  # Ck+1
        frequentSet = calculateMinimumSupport(candidateSet, transactionSet)                                 # Lk+1
        k += 1

    # Sorting in descending order of Support
    sortedSet = sorted(finalFreqSet.items(), key=operator.itemgetter(1), reverse=True)

    # Creating a dictionary for the vocab
    vocabFile = open(sys.argv[2], 'r')
    for line in vocabFile:
        k, v = line.split()
        vocabDictionary[k] = v

    # Writing the frequent patterns to a file
    patternFile = open(sys.argv[3], 'w')
    for value in sortedSet:
        pattern = ""
        for i in list(value[0]):
            pattern = pattern + " " + vocabDictionary[i]
        patternFile.write("%i %s \n" % (value[1], pattern))


# import data from the topic file
def extractData():
    sourceFile = open(sys.argv[1], 'r')
    for line in sourceFile:
        transaction = frozenset(line.split())
        yield transaction


# Generate 1-item set candidates
def generatetOneItemSetCandidates(topicData):
    itemSet = set()
    transactionSet = list()
    for tran in topicData:
        transaction = frozenset(tran)
        transactionSet.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))
    return itemSet, transactionSet


# Calculate Minimum Support
def calculateMinimumSupport(itemSet, transactionSet):
    prunedSet = set()
    tempSet = defaultdict(int)
    for item in itemSet:
        for transaction in transactionSet:
                if item.issubset(transaction):
                        tempSet[item] += 1
    for key, value in tempSet.items():
        if value >= minSupport:
                prunedSet.add(key)
                finalFreqSet[key] = value
    return prunedSet


if __name__ == "__main__":
    minSupport = 50  # Defining the minimum support
    finalFreqSet = {}
    main()

