import pandas as pd
from conllu import parse, parse_incr
from itertools import combinations, combinations_with_replacement

udpipeOutputFile = open('output.txt', 'r')
udpipeOutputFileInt = open('cleanedOutput.txt', 'w')

drugBaseFile = open('drugBase.txt','r')
drugBase1 = []
drugBase2 = []
drugBase3 = []
drugBase4 = []
drugBase5 = []
drugBase6 = []

for line in drugBaseFile:
    if len(line.split()) == 1:
        drugBase1.append(line.split("\n")[0].lower())
    elif len(line.split()) == 2:
        drugBase2.append(line.split("\n")[0].lower())
    elif len(line.split()) == 3:
        drugBase3.append(line.split("\n")[0].lower())
    elif len(line.split()) == 4:
        drugBase4.append(line.split("\n")[0].lower())
    elif len(line.split()) == 5:
        drugBase5.append(line.split("\n")[0].lower())
    elif len(line.split()) == 6:
        drugBase6.append(line.split("\n")[0].lower())

with open('drugBase1.txt', 'w') as f:
    for item in drugBase1:
        f.write("%s\n" % item)
with open('drugBase2.txt', 'w') as f:
    for item in drugBase2:
        f.write("%s\n" % item)

with open('drugBase3.txt', 'w') as f:
    for item in drugBase3:
        f.write("%s\n" % item)

with open('drugBase4.txt', 'w') as f:
    for item in drugBase4:
        f.write("%s\n" % item)

with open('drugBase5.txt', 'w') as f:
    for item in drugBase5:
        f.write("%s\n" % item)


def isDrug(drugName):
    drugIsInList = 0
    if drugName in drugBase1:
        drugIsInList = 1
    if drugName in drugBase2:
        drugIsInList = 2
    if drugName in drugBase3:
        drugIsInList = 3
    if drugName in drugBase4:
        drugIsInList = 4
    if drugName in drugBase5:
        drugIsInList = 5
    if drugName in drugBase6:
        drugIsInList = 6

    return drugIsInList



# maxLenDrugName = max(drugBase, key = len)
#
# print("Longest drug name: ", maxLenDrugName)
# maxLenDrugNameList = maxLenDrugName.split(" ")
# maxLenDrugNameLength = len(maxLenDrugNameList)
# print("max words in drug name: ", maxLenDrugNameLength)

count = 0
sentences = []
for line in udpipeOutputFile:
    aLine = line.split(" ")
    aLineClean = line.rstrip('\n').rstrip('.').split(" ")
    if aLine[0] != '#':
            udpipeOutputFileInt.write(line)
    else:
        if aLine[1] == 'text':
            sentences.append(aLineClean[3:])

def getCombinations(lineNo):
    # for i in range(len(sentences)):
    drugNames = []
    drugFound = []
    drugFoundin = []
    for start, end in combinations(range(len(sentences[lineNo])), 2):
        if len(sentences[lineNo][start:end+1]) < 5:
            drugNames.append(sentences[lineNo][start:end+1])
    drugNames.sort(key=lambda s:len(s),reverse=True)
    for i in drugNames:
        drugName = " ".join(i)
        if isDrug(drugName) != 0:
            drugFoundin.append(isDrug(drugName.lower()))
            drugFound.append(i)
        print(drugFound)
    return drugFoundin, drugFound


# print(drugBase)
udpipeOutputFileInt.close()

udpipeOutputFile = open('cleanedOutput.txt', 'r')
udpipeOutputFileTraining = open('trainingSet.txt', 'w')

# print(sentences)
lineNo = 0

for line in udpipeOutputFile:
    aLine = line.split("\t")
    drugFoundin = []
    drugFound = []
    if aLine[0] != '\n':
        drugFoundin, drugFound = getCombinations(lineNo)
        if len(drugFound) != 0:
            aLine[4] = 'BO'
            newLine = "\t".join(aLine)
            udpipeOutputFileTraining.write(newLine)
            if len(drugFound) > 1:
                for iter in range(len(drugFound)):
                    nextLine = next(line).split("\t")
                    nextLine[4] = 'IO'
                    nextLine = "\t".join(aLine)
                    udpipeOutputFileTraining.write(nextLine)
        else:
            aLine[4] = 'BO'
            newLine = "\t".join(aLine)
            udpipeOutputFileTraining.write(newLine)
    else:
        udpipeOutputFileTraining.write('\n')
        lineNo += 1


udpipeOutputFileTraining.close()