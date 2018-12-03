import xml.etree.ElementTree as ET
import pandas as pd
import os

#  *******************************START:Code to generate TSV file for Pair Master data ************************
def xmldata(fileName, xml_data):
    parsed_xml = ET.parse(fileName)
    root = parsed_xml.getroot()
    testCase = 'DDI2013'
    print(fileName)
    sentenceTag = root.findall('sentence')
    dataFrameColumnsP = ['Pair_Id', 'E2', 'E1','DDI', 'type']
    xml_dataP = pd.DataFrame(columns=dataFrameColumnsP)

    for sentence in sentenceTag:
        pairTags = sentence.findall('pair')
        for tag in pairTags:
            if tag.attrib.get('ddi') == 'true':
                xml_dataP = xml_dataP.append(pd.Series([tag.attrib.get('id'), tag.attrib.get('e1'),
                                                        tag.attrib.get('e2'), tag.attrib.get('ddi'),
                                                        tag.attrib.get('type')],
                                                       index=dataFrameColumnsP), ignore_index=True)
            else:
                xml_dataP = xml_dataP.append(pd.Series([tag.attrib.get('id'), tag.attrib.get('e1'),
                                                        tag.attrib.get('e2'), tag.attrib.get('ddi'),
                                                        'None'],
                                                       index=dataFrameColumnsP), ignore_index=True)
    frames = [xml_data, xml_dataP]
    xml_data =pd.concat(frames)
    return  xml_data

Path = "D:/University/Sem1/Linguistics/Project/drugbank_all_full_database/semeval_task9_train_pair/Train/DrugBank"
filelist = os.listdir(Path)

dataFrameColumnsP = ['Pair_Id', 'E2', 'E1']
xml_data = pd.DataFrame(columns=dataFrameColumnsP)

count  = 0
for i in filelist:
    if i.endswith(".xml"):
        # if count < 1:
        xml_data = xmldata("DrugBank/" + i, xml_data)

print(xml_data)

xml_data.to_csv("DrugPair_MasterData.tsv",sep="\t")

#  *******************************END:Code to generate TSV file for Pair Master data ************************