__author__ = 'suma'

from collections import defaultdict
import operator
import sys


def main():
    # import data from frequent pattern file
    sourceFile = open(sys.argv[1], 'r')
    transactions = []
    dict = {}
    for line in sourceFile:
        split_line = line.split()
        value = split_line[0]
        del split_line[0]
        dict[frozenset(split_line)] = value
        transactions.append(split_line)

    # For each frequent item set find out if there exists any frequent super-pattern
    maxPatternSet = defaultdict(int)
    for key1, value1 in dict.iteritems():
        superPatternFound = False
        for key2, value2 in dict.iteritems():
            if key1 == key2:
                continue
            elif key1.issubset(key2):
                superPatternFound = True
                break
        if superPatternFound == False:
            maxPatternSet[key1] = int(value1)

    # Sort in descending order of Support
    sortedSet = sorted(maxPatternSet.items(), key=operator.itemgetter(1), reverse=True)

    # Write all the max patterns to a file
    maxPatternFile = open(sys.argv[2], 'w')
    for value in sortedSet:
        pattern = ""
        for i in list(value[0]):
            pattern = pattern + " " + i
        maxPatternFile.write("%i %s \n" % (value[1], pattern))


if __name__ == "__main__":
    main()