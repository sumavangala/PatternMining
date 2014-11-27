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

    # Reading pattern files
    patternSourceFile1 = open(sys.argv[2], 'r')
    patternDict1 = {}
    for line in patternSourceFile1:
        split_line = line.split()
        value = split_line[0]
        del split_line[0]
        patternDict1[frozenset(split_line)] = int(value)

    patternSourceFile2 = open(sys.argv[3], 'r')
    patternDict2 = {}
    for line in patternSourceFile2:
        split_line = line.split()
        value = split_line[0]
        del split_line[0]
        patternDict2[frozenset(split_line)] = int(value)

    patternSourceFile3 = open(sys.argv[4], 'r')
    patternDict3 = {}
    for line in patternSourceFile3:
        split_line = line.split()
        value = split_line[0]
        del split_line[0]
        patternDict3[frozenset(split_line)] = int(value)

    patternSourceFile4 = open(sys.argv[5], 'r')
    patternDict4 = {}
    for line in patternSourceFile4:
        split_line = line.split()
        value = split_line[0]
        del split_line[0]
        patternDict4[frozenset(split_line)] = int(value)

    patternSourceFile5 = open(sys.argv[6], 'r')
    patternDict5 = {}
    for line in patternSourceFile5:
        split_line = line.split()
        value = split_line[0]
        del split_line[0]
        patternDict5[frozenset(split_line)] = int(value)

    return patternDict1, patternDict2, patternDict3, patternDict4, patternDict5


def main():
    patternDict1, patternDict2, patternDict3, patternDict4, patternDict5 = readFromSourceFiles()
    for key, value in patternDict1.iteritems():
        freq1 = value  # f(t,p)

        freq2 = 0
        if key in patternDict2:
            freq2 = patternDict2[key]

        freq3 = 0
        if key in patternDict3:
            freq3 = patternDict3[key]

        freq4 = 0
        if key in patternDict4:
            freq4 = patternDict4[key]

        freq5 = 0
        if key in patternDict5:
            freq5 = patternDict5[key]

        # purity(p,t)=log[f(t,p)/|D(t)|] - log(max[(f(t,p)+f(t',p))/|D(t,t')|])
        purity = math.log((freq1*1.0)/int(sys.argv[8]), math.e) - math.log(max(((freq1+freq2)*1.0)/int(sys.argv[9]), ((freq1+freq3)*1.0)/int(sys.argv[10]), ((freq1+freq4)*1.0)/int(sys.argv[11]), ((freq1+freq5)*1.0)/int(sys.argv[12])), math.e)
        finalFreqSet.append([key, round(purity, 4), int(value)])

if __name__ == "__main__":
    finalFreqSet = []
    main()
    # Sort in descending order of Purity and Support
    sortedSet = sorted(finalFreqSet, key=operator.itemgetter(1, 2), reverse=True)

    # Write all patterns to a file
    purityFile = open(sys.argv[7], 'w')
    for value in sortedSet:
        pattern = ""
        for i in list(value[0]):
            pattern = pattern + " " + i
        purityFile.write("%.4f %s \n" % (value[1], pattern))