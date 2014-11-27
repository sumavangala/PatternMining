__author__ = 'suma'


import math
import operator
import sys


def readFromSourceFiles():
    # Creating a dictionary for the vocab
    vocabDictionary = {}
    vocabFile = open(sys.argv[1], 'r')
    for line in vocabFile:
        k, v = line.split()
        vocabDictionary[k] = v

    patternFile = open(sys.argv[2], "r")
    topic0Dict = {}
    for line in patternFile:
        split_line = line.split()
        value = split_line[0]
        del split_line[0]
        topic0Dict[frozenset(split_line)] = int(value)

    topic0SourceFile = open(sys.argv[3], "r")
    topic0Transactions = []
    for line in topic0SourceFile:
        split_line = line.split()
        newSet = []
        for i in split_line:
            newSet.append(vocabDictionary[i])
        topic0Transactions.append(newSet)

    topic1SourceFile = open(sys.argv[4], "r")
    topic1Transactions = []
    for line in topic1SourceFile:
        split_line = line.split()
        newSet = []
        for i in split_line:
            newSet.append(vocabDictionary[i])
        topic1Transactions.append(newSet)

    topic2SourceFile = open(sys.argv[5], "r")
    topic2Transactions = []
    for line in topic2SourceFile:
        split_line = line.split()
        newSet = []
        for i in split_line:
            newSet.append(vocabDictionary[i])
        topic2Transactions.append(newSet)

    topic3SourceFile = open(sys.argv[6], "r")
    topic3Transactions = []
    for line in topic3SourceFile:
        split_line = line.split()
        newSet = []
        for i in split_line:
            newSet.append(vocabDictionary[i])
        topic3Transactions.append(newSet)

    topic4SourceFile = open(sys.argv[7], "r")
    topic4Transactions = []
    for line in topic4SourceFile:
        split_line = line.split()
        newSet = []
        for i in split_line:
            newSet.append(vocabDictionary[i])
        topic4Transactions.append(newSet)

    return topic0Dict, topic0Transactions, topic1Transactions, topic2Transactions, topic3Transactions, topic4Transactions


def main():
    topic0Dict, topic0Transactions, topic1Transactions, topic2Transactions, topic3Transactions, topic4Transactions = readFromSourceFiles()
    for key, value in topic0Dict.iteritems():
        freq0 = value  # f(t,p)
        freq1 = 0
        for tran in topic1Transactions:
            if key.issubset(tran):
                freq1 += 1
        freq2 = 0
        for tran in topic2Transactions:
            if key.issubset(tran):
                freq1 += 1
        freq3 = 2
        for tran in topic3Transactions:
            if key.issubset(tran):
                freq3 += 1
        freq4 = 0
        for tran in topic4Transactions:
            if key.issubset(tran):
                freq4 += 1

        sum = 0
        if len(key) > 1:
            for word in key:
                freq = 0
                for tran in topic0Transactions:
                    if word in tran:
                        freq += 1
                sum += math.log((freq*1.0)/10047, math.e)

        # purity(p,t)=log[f(t,p)/|D(t)|] - log(max[(f(t,p)+f(t',p))/|D(t,t')|])
        # |D(t0)|=10047, |D(t0,t1)|=17326, |D(t0,t2)|=17988, |D(t0,t3)|=17999, |D(t0,t4)|=17820
        # |D(t1)|=9674,  |D(t1,t0)|=17326, |D(t1,t2)|=17446, |D(t1,t3)|=17902, |D(t1,t4)|=17486
        # |D(t2)|=9959,  |D(t2,t0)|=17988, |D(t2,t1)|=17446, |D(t2,t3)|=18077, |D(t2,t4)|=17492
        # |D(t3)|=10161, |D(t3,t0)|=17999, |D(t3,t1)|=17902, |D(t3,t2)|=18077, |D(t3,t4)|=17912
        # |D(t4)|=9845,  |D(t4,t0)|=17820, |D(t4,t1)|=17486, |D(t4,t2)|=17492, |D(t4,t3)|=17912

        purity = math.log((freq0*1.0)/10047, math.e) - math.log(max(((freq0+freq1)*1.0)/17326, ((freq0+freq2)*1.0)/17988, ((freq0+freq3)*1.0)/17999, ((freq0+freq4)*1.0)/17820), math.e)
        coverage = (freq0*1.0)/10047
        phraseness = math.log((freq0*1.0)/10047, math.e) - sum

        # rank = coverage[(1-w)purity + w * phraseness] W = 0.1
        rank = coverage * (((1-0.1) * purity) + (0.1 * phraseness))
        rankSet[key] = rank

if __name__ == "__main__":
    rankSet = {}
    main()

    # Sort in descending order of rank
    sortedRankSet = sorted(rankSet.items(), key=operator.itemgetter(1), reverse=True)

    # Write all patterns to a file
    maxPatternFile = open("ReRank-0.txt", 'w')
    for value in sortedRankSet:
        pattern = ""
        for i in list(value[0]):
            pattern = pattern + " " + i
        maxPatternFile.write("%.4f %s \n" % (value[1], pattern))