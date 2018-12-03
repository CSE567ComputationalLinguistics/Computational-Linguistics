import pandas as pd
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import os

#  *******************************START:Code to generate TSV file for Pair Master data ************************
# def xmldata(fileName, xml_data):
#     parsed_xml = ET.parse(fileName)
#     root = parsed_xml.getroot()
#     testCase = 'DDI2013'
#     print(fileName)
#     sentenceTag = root.findall('sentence')
#     dataFrameColumnsP = ['Pair_Id', 'E2', 'E1']
#     xml_dataP = pd.DataFrame(columns=dataFrameColumnsP)
#
#     for sentence in sentenceTag:
#         pairTags = sentence.findall('pair')
#         for tag in pairTags:
#             xml_dataP = xml_dataP.append(pd.Series([tag.attrib.get('id'), tag.attrib.get('e1'),
#                                                     tag.attrib.get('e2')],
#                                                    index=dataFrameColumnsP), ignore_index=True)
#
#     frames = [xml_data, xml_dataP]
#     xml_data =pd.concat(frames)
#     return  xml_data
#
# Path = "D:/University/Sem1/Linguistics/Project/drugbank_all_full_database/semeval_task9_train_pair/Test/test"
# filelist = os.listdir(Path)
#
# dataFrameColumnsP = ['Pair_Id', 'E2', 'E1']
# xml_data = pd.DataFrame(columns=dataFrameColumnsP)
#
# count  = 0
# for i in filelist:
#     if i.endswith(".xml"):
#         # if count < 1:
#         xml_data = xmldata("test/" + i,xml_data)
#
# print(xml_data)
#
# xml_data.to_csv("DrugPair_MasterData.tsv",sep="\t")

#  *******************************END:Code to generate TSV file for Pair Master data ************************

xml_data = pd.read_csv('DrugPair_MasterData.tsv', sep='\t')
xml_data.columns = ["PairID", "Entity1ID", "Entity2ID"]

trainResult = pd.read_csv('TestResultCleaning.txt', sep="\t", header=None)
trainResult.columns = ["Entity1ID", "Entity2ID", "PredictedLabel"]

dataFrameColumnsP = ['TestCase','Pair_Id', 'Prediction']
xml_dataWithPairID = pd.DataFrame(columns=dataFrameColumnsP)

# print(trainResult)
# print(xml_data)

trainResultArray = trainResult.values

# print(trainResult[(trainResult[['Entity1ID', 'Entity2ID']].isin(xml_data[['Entity1ID', 'Entity2ID']]))])

for i in range(len(trainResultArray)):
    index_list.append(xml_data[(xml_data['Entity1ID'] == trainResultArray[i][0]) &
                          (xml_data['Entity2ID'] == trainResultArray[i][1])].index.tolist())

    print(trainResultArray[i][0], trainResultArray[i][1])
    print(xml_data.iloc[index_list[i],0])

print(index_list)







