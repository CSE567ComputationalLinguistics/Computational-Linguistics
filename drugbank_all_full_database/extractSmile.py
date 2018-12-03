import xml.etree.ElementTree as ET
import pandas as pd
import os
count = 0
# def getDrugName(drugID, root, count):
#     count += 1
#     drugName = None
#     print("For: ",drugID)
#     for drug in root:
#         drugBankIds = drug.findall('{http://www.drugbank.ca}drugbank-id')
#         for drugBankId in drugBankIds:
#             if drugBankId.text == drugID:
#                 drugName = drug.find('{http://www.drugbank.ca}name').text
#                 print(drugName)
#                 break
#
#     return drugName, count
#
#
# Path = "D:/University/Sem1/Linguistics/Project/drugbank_all_full_database/ddi"
# filelist = os.listdir(Path)
#
# drugMasterDataColumns = ['DrugID', 'DrugName']
# drugMasterData = pd.DataFrame(columns=drugMasterDataColumns)
#
# parsed_xml_drugBank = ET.parse("full_database.xml")
# root = parsed_xml_drugBank.getroot()
# print("Completed Parsing \n")
#
# for i in filelist:
#     if i.endswith(".smiles"):
#         drugID = i.split(".", 1)[0]
#
#         drugName, count = getDrugName(drugID, root, count)
#
#         drugMasterData = drugMasterData.append(
#             pd.Series([drugID, drugName],
#                       index=drugMasterDataColumns), ignore_index=True
#         )
#
# print(count)
# table = drugMasterData
# writer = pd.ExcelWriter('drugMasterData.xlsx')
# table.to_excel(writer,'Sheet1')
# writer.save()
#
# Path = "D:/University/Sem1/Linguistics/Project/drugbank_all_full_database/semeval_task9_train_pair/Train/DrugBank"
# filelist = os.listdir(Path)
#
# drugNameColumns = ['DrugName']
# drugNameDF = pd.DataFrame(columns=drugNameColumns)
#
# for i in filelist:
#     if i.endswith(".xml"):
#         drugName = i.split("_", 1)[0]
#         drugNameDF = drugNameDF.append(
#                         pd.Series([drugName],
#                                   index=drugNameColumns), ignore_index=True
#         )
#
# table = drugNameDF
# writer = pd.ExcelWriter('drugNames.xlsx')
# table.to_excel(writer,'Sheet1')
# writer.save()

#  To change extgension of the smile files
Path = "D:/University/Sem1/Linguistics/Project/drugbank_all_full_database/ddi"
filelist = os.listdir(Path)

for i in filelist:
     if i.endswith(".smiles"):
          infilename = os.path.join(Path, i)
          print(infilename)
          if not os.path.isfile(infilename): continue
          oldbase = os.path.splitext(i)
          newname = infilename.replace('.smiles', '.smi')
          output = os.rename(infilename, newname)