import xml.etree.ElementTree as ET
import pandas as pd
import os

def xmldata(fineName, xml_data):
    parsed_xml = ET.parse(fineName)
    root = parsed_xml.getroot()
    print(fineName)
    dataFrameColumnsE = ['Document_id', 'Sentence_ID', 'Sentence_Text', 'Entity_Id', 'Entity_Text', 'Entity_type', 'CharOffset']
    dataFrameColumnsP = ['Document_id', 'Sentence_ID', 'Sentence_Text', 'Pair_Id', 'DDI', 'E2', 'E1']

    xml_dataE = pd.DataFrame(columns=dataFrameColumnsE)
    xml_dataP = pd.DataFrame(columns=dataFrameColumnsP)
    #print(root.tag,root.attrib)
    sentencesNode = root.findall('sentence')
    for sentence in sentencesNode:
        #print(sentence.tag,sentence.attrib)
        for node in sentence.getiterator():
            #print(node.tag, node.attrib)
            
            if node.tag=='entity':

                xml_dataE = xml_dataE.append(pd.Series([root.attrib.get('id'), sentence.attrib.get('id'),
                                        sentence.attrib.get('text'), node.attrib.get('id'),
                                       node.attrib.get('text'), node.attrib.get('type'),
                                       node.attrib.get('charOffset')],
                                      index=dataFrameColumnsE), ignore_index=True
                        )
            elif node.tag=='pair':
                
                xml_dataP = xml_dataP.append(pd.Series([root.attrib.get('id'),sentence.attrib.get('id'),
                                        sentence.attrib.get('text'), node.attrib.get('id'),
                                       node.attrib.get('ddi'),node.attrib.get('e2'),
                                       node.attrib.get('e1')],
                                      index=dataFrameColumnsP),ignore_index=True)
            xml_data = pd.concat([xml_data, xml_dataE, xml_dataP], axis=0, ignore_index=True, sort=False)
    return xml_data



Path = "D:/University/Sem1/Linguistics/Project/drugbank_all_full_database/semeval_task9_train_pair/Train/DrugBank"
filelist = os.listdir(Path)

dataFrameColumns = ['Document_id','Sentence_ID','Sentence_Text','Entity_Id','Entity_Text',
                    'Entity_type','CharOffset','Pair_Id','DDI','E2','E1']
xml_data = pd.DataFrame(columns=dataFrameColumns)
print("No of Drug Files in DrugBank Database: ",len(filelist))
for i in filelist:
    if i.endswith(".xml"):
        xml_data = xmldata("DrugBank/"+i, xml_data)

Path = "D:/University/Sem1/Linguistics/Project/drugbank_all_full_database/semeval_task9_train_pair/Train/MedLine"
filelist = os.listdir(Path)

print("No of Drug Files in MedLine Database: ", len(filelist))
for i in filelist:
    if i.endswith(".xml"):
      xml_data = xmldata("MedLine/" + i, xml_data)

writer = pd.ExcelWriter("merged1.xlsx")
xml_data.to_excel(writer, 'sheet1')
writer.save()





