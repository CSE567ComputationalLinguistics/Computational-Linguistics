import xml.etree.ElementTree as ET
import pandas as pd
import os


def xmldata(fileName, xml_data):
    parsed_xml = ET.parse(fileName)
    root = parsed_xml.getroot()
    print(fileName)
    dataFrameColumnsE = ['Document_id', 'Sentence_ID','Sentence', 'Entity_Id', 'Entity_Text']
    dataFrameColumnsP = ['Document_id', 'Sentence_ID','Sentence', 'Pair_Id', 'E2', 'E1', 'DDI']
    dataFrameColumns = ['Document_id', 'Sentence_ID','Sentence', 'Entity_Id', 'Entity_Text',
                        'Pair_Id', 'E2', 'E1', 'DDI']
    xml_data_temp = pd.DataFrame(columns=dataFrameColumns)
    xml_dataE = pd.DataFrame(columns=dataFrameColumnsE)
    xml_dataP = pd.DataFrame(columns=dataFrameColumnsP)
    sentencesNode = root.findall('sentence')
    for sentence in sentencesNode:
        for node in sentence.getiterator():
            if node.tag == 'entity':

                xml_dataE = xml_dataE.append(pd.Series([root.attrib.get('id'), sentence.attrib.get('id'),sentence.text,
                                                        node.attrib.get('id'), node.attrib.get('text')],
                                                       index=dataFrameColumnsE), ignore_index=True
                                             )
            elif node.tag == 'pair':

                xml_dataP = xml_dataP.append(pd.Series([root.attrib.get('id'), sentence.attrib.get('id'),sentence.text,
                                                        node.attrib.get('id'), node.attrib.get('e2'),
                                                        node.attrib.get('e1'), node.attrib.get('ddi')],
                                                       index=dataFrameColumnsP), ignore_index=True)
            xml_data_temp = pd.merge( xml_dataP, xml_dataE,on=['Document_id', 'Sentence_ID'])
            xml_data = pd.concat([xml_data, xml_data_temp], axis=0, ignore_index=True, sort=False)
    return xml_data


Path = "/home/csgrad/chinmayp/semeval_task9_train_pair/Train/DrugBank"
filelist = os.listdir(Path)

dataFrameColumns = ['Document_id', 'Sentence_ID','Sentence', 'Entity_Id', 'Entity_Text',
                    'Pair_Id', 'E2', 'E1', 'DDI']
xml_data = pd.DataFrame(columns=dataFrameColumns)
print("No of Drug Files in DrugBank Database: ", len(filelist))
#count = 0
for i in filelist:
    if i.endswith(".xml"):
#        if count < 1:
         xml_data = xmldata("Train/DrugBank/" + i, xml_data)
#           count += 1

#Path = "/home/csgrad/chinmayp/semeval_task9_train_pair/Train/MedLine"
#filelist = os.listdir(Path)

#print("No of Drug Files in MedLine Database: ", len(filelist))
#count = 0
#for i in filelist:
#    if i.endswith(".xml"):
#        if count < 1:
#            xml_data = xmldata("Train/MedLine/" + i, xml_data)
#            count += 1

print("writing excel file")
writer = pd.ExcelWriter("merged1.xlsx")
xml_data.to_excel(writer, 'sheet1')
writer.save()