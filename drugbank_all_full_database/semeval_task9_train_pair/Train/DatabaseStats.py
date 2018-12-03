import xml.etree.ElementTree as ET
import pandas as pd
import os

Path = "D:/University/Sem1/Linguistics/Project/drugbank_all_full_database/semeval_task9_train_pair/Train/DrugBank"
filelist = os.listdir(Path)
countDrugBank = 0
countDrugBankEntities = 0
countDrugBankPair = 0
print("************************************ Drug Bank Stats *****************************************")

print("No of Drug Files in DrugBank Database: ",len(filelist))
for i in filelist:
    if i.endswith(".xml"):
        parsed_xml_drugBank = ET.parse("DrugBank/"+i)
        root = parsed_xml_drugBank.getroot()
        sentences = root.findall('sentence')
        countDrugBank = countDrugBank + len(sentences)
        for sentence in sentences:
            countDrugBankEntities = countDrugBankEntities + len(sentence.findall('entity'))
            countDrugBankPair = countDrugBankPair + len(sentence.findall('pair'))

print("No of Sentences in DrugBank Database: ",countDrugBank)
print("No of entities in DrugBank Database: ",countDrugBankEntities)
print("Avegrage no of entities in DrugBank Database: ",countDrugBankEntities / countDrugBank)
print("No of Pairs in DrugBank Database: ",countDrugBankPair)
print("Avegrage no of Pairs in DrugBank Database: ",countDrugBankPair / countDrugBank)

print("************************************ MedLine Stats *****************************************")

Path = "D:/University/Sem1/Linguistics/Project/drugbank_all_full_database/semeval_task9_train_pair/Train/MedLine"
filelist = os.listdir(Path)
countMedLine = 0
countMedLineEntities = 0
countMedLinePair = 0
print("No of Drug Files in MedLine Database: ",len(filelist))
for i in filelist:
    if i.endswith(".xml"):
        parsed_xml_MedLine = ET.parse("MedLine/"+i)
        root = parsed_xml_MedLine.getroot()
        sentenceMedLine = root.findall('sentence')
        countMedLine = countMedLine + len(sentenceMedLine)
        for sentence in sentenceMedLine:
            countMedLineEntities = countMedLineEntities + len(sentence.findall('entity'))
            countMedLinePair = countMedLinePair + len(sentence.findall('pair'))

print("No of Sentences in MedLine Database: ",countMedLine)
print("No of entities in DrugBank Database: ",countMedLineEntities)
print("Avegrage no of entities in DrugBank Database: ",countMedLineEntities / countMedLine)
print("No of Pairs in DrugBank Database: ",countMedLinePair)
print("Avegrage no of Pairs in DrugBank Database: ",countMedLinePair / countMedLine)


