import pandas as pd
from conllu import parse, parse_incr


udpipeOutputFile = open('drugLemma.txt', 'r')
udpipeOutputFileInt = open('cleaneddrugLemma.txt', 'w')
udpipeOutputFileFinal = open('lemmatizedDrugBase.txt', 'w')

for line in udpipeOutputFile:
    aLine = line.split(" ")
    if aLine[0] != '#':
            udpipeOutputFileInt.write(line)

udpipeOutputFileInt.close()

udpipeOutputFileInt = open('cleaneddrugLemma.txt', 'r')

drugName =""
for line in udpipeOutputFileInt:
    aLine = line.split("\t")
    if aLine[0] !="\n":
        if aLine[5] == "Number=Plur":
           if aLine[9] =="SpaceAfter=No\n":
               if drugName == "":
                   drugName = aLine[2]
               else:
                   drugName = drugName+aLine[2]
           else:
                if aLine[9] =="SpacesAfter=\\r\\n\n":
                   if drugName == "":
                       drugName = aLine[2]
                   else:
                       drugName = drugName+aLine[2]
                else:
                   if drugName == "":
                       drugName = aLine[2]+" "
                   else:
                       drugName = drugName+aLine[2]+" "
        else:
            if aLine[9] == "SpaceAfter=No\n":
                if drugName == "":
                    drugName = aLine[1]
                else:
                    drugName = drugName + aLine[1]
            else:
                if aLine[9] =="SpacesAfter=\\r\\n\n":
                   if drugName == "":
                       drugName = aLine[1]
                   else:
                       drugName = drugName+aLine[1]
                else:
                   if drugName == "":
                       drugName = aLine[1]+" "
                   else:
                       drugName = drugName+aLine[1]+" "
    else:
        udpipeOutputFileFinal.write(drugName.lower()+"\n")
        drugName =""

udpipeOutputFileFinal.close()

# udpipeOutputFileFinal = open('lemmatizedDrugBase.txt', 'r+')
#
# for line in udpipeOutputFileFinal:
#     drugName = line.rstrip(" ")
#     print(drugName)
#     udpipeOutputFileFinal.write(drugName)
#
# udpipeOutputFileFinal.close()