import pandas as pd

udpipeOutputFile = open('trainingFile.txt', 'r')
udpipeOutputFileInt = open('cleanedResultUdpipe.txt','w')
drugAnnotatedFile = open('result.udpiped', 'r')

resultNer = open('result.ner','r')
resultNerCleaned = open('resultnerCleaned.txt','w')

for line in drugAnnotatedFile:
    aLine = line.split(" ")
    aLineClean = line.rstrip('\n').rstrip('.').split(" ")
    if aLine[0] != '#':
        udpipeOutputFileInt.write(line)

udpipeOutputFileInt.close()

identifiedDrugs = []
sentenceNumber = 0
info = []
for line in resultNer:
    info = []
    aLine = line.split("\t")
    if len(aLine) == 2:
        aLine.append(sentenceNumber)
        info.append(sentenceNumber)
        info.append((aLine[0].split(",")[0]))
        identifiedDrugs.append(info)
    if aLine[0] == '\n':
        sentenceNumber += 1

print(identifiedDrugs)
