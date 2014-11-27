#!/bin/sh

vocab="DataFiles/vocab.txt"
topic0="DataFiles/topic-0.txt"
topic1="DataFiles/topic-1.txt"
topic2="DataFiles/topic-2.txt"
topic3="DataFiles/topic-3.txt"
topic4="DataFiles/topic-4.txt"

pattern0="patterns/pattern-0.txt"
pattern1="patterns/pattern-1.txt"
pattern2="patterns/pattern-2.txt"
pattern3="patterns/pattern-3.txt"
pattern4="patterns/pattern-4.txt"

max0="max/max-0.txt"
max1="max/max-1.txt"
max2="max/max-2.txt"
max3="max/max-3.txt"
max4="max/max-4.txt"

closed0="closed/closed-0.txt"
closed1="closed/closed-1.txt"
closed2="closed/closed-2.txt"
closed3="closed/closed-3.txt"
closed4="closed/closed-4.txt"

purity0="purity/purity-0.txt"
purity1="purity/purity-1.txt"
purity2="purity/purity-2.txt"
purity3="purity/purity-3.txt"
purity4="purity/purity-4.txt"

Dt0=10047
Dt0t1=17326
Dt0t2=17988
Dt0t3=17999
Dt0t4=17820
Dt1=9674
Dt1t2=17446
Dt1t3=17902
Dt1t4=17486
Dt2=9959
Dt2t3=18077
Dt2t4=17492
Dt3=10161
Dt3t4=17912
Dt4=9845

# Generate frequent patterns
mkdir patterns
printf "Generating frequent patterns...\n"
python AprioriFrequentPatternMining.py $topic0 $vocab $pattern0
python AprioriFrequentPatternMining.py $topic1 $vocab $pattern1
python AprioriFrequentPatternMining.py $topic2 $vocab $pattern2
python AprioriFrequentPatternMining.py $topic3 $vocab $pattern3
python AprioriFrequentPatternMining.py $topic4 $vocab $pattern4
printf "Generating frequent patterns completed\n"

# Generate maximal patterns
mkdir max
printf "Generating max patterns...\n"
python MaxPatterns.py $pattern0 $max0
python MaxPatterns.py $pattern1 $max1
python MaxPatterns.py $pattern2 $max2
python MaxPatterns.py $pattern3 $max3
python MaxPatterns.py $pattern4 $max4
printf "Generating max patterns completed\n"

# Generate closed patterns
mkdir closed
printf "Generating closed patterns...\n"
python ClosedPatterns.py $pattern0 $closed0
python ClosedPatterns.py $pattern1 $closed1
python ClosedPatterns.py $pattern2 $closed2
python ClosedPatterns.py $pattern3 $closed3
python ClosedPatterns.py $pattern4 $closed4
printf "Generating closed patterns completed\n"

# ReRank by Purity
mkdir purity
printf "Generating patterns reranked by purity...\n"
python ReRankByPurity.py $vocab $pattern0 $pattern1 $pattern2 $pattern3 $pattern4 $purity0 $Dt0 $Dt0t1 $Dt0t2 $Dt0t3 $Dt0t4
python ReRankByPurity.py $vocab $pattern1 $pattern0 $pattern2 $pattern3 $pattern4 $purity1 $Dt1 $Dt0t1 $Dt1t2 $Dt1t3 $Dt1t4
python ReRankByPurity.py $vocab $pattern2 $pattern0 $pattern1 $pattern3 $pattern4 $purity2 $Dt2 $Dt0t2 $Dt1t2 $Dt2t3 $Dt2t4
python ReRankByPurity.py $vocab $pattern3 $pattern0 $pattern1 $pattern2 $pattern4 $purity3 $Dt3 $Dt0t3 $Dt1t3 $Dt2t3 $Dt3t4
python ReRankByPurity.py $vocab $pattern4 $pattern0 $pattern1 $pattern2 $pattern3 $purity4 $Dt4 $Dt0t4 $Dt1t4 $Dt2t4 $Dt3t4
printf "Generating patterns reranked by purity completed\n"

# ReRanking - bonus question
printf "Generating patterns reranked by purity, phraseness and coverage...\n"
python ReRanking.py $vocab $pattern0 $topic0 $topic1 $topic2 $topic3 $topic4
printf "Generating patterns reranked by purity, phraseness and coverage\n"
