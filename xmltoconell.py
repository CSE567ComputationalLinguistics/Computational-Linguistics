import xml.etree.ElementTree as ET
import pandas as pd

def getnodeval(node):
    if node is not None:
        return node.text

def xmldata():
    parsed_xml = ET.parse("ADCIRCA_ff61b237-be8e-461b-8114-78c52a8ad0ae.xml")
    root = parsed_xml.getroot()
    print(root)
    dataFrameColumns = ['Label_Set_ID','DrugName','Sentence_ID','Sentence_Text','Mention_ID']#,'LabelDrug','SentenceSectionID']
    xml_data = pd.DataFrame(columns=dataFrameColumns)
    print(root.tag,root.attrib)
    sentencesNode = root.findall('Sentences')

    for sentence in sentencesNode:
        for node in sentence.getiterator():
            # print(node.tag, node.attrib,node.text)

            if node.tag == "Sentence":
                sentenceText = node.find('SentenceText')
                Mentions = node.findall('Mention')
                if Mentions != None:
                    for mention in Mentions:
                        xml_data = xml_data.append(
                            pd.Series([root.attrib.get('setid'), root.attrib.get('drug'),node.attrib.get('id'),
                                       sentenceText.text, mention.attrib.get('id')],
                                      index=dataFrameColumns),ignore_index=True
                        )
                else:
                    xml_data = xml_data.append(
                        pd.Series([root.attrib.get('setid'), root.attrib.get('drug'), node.attrib.get('id'),
                                   sentenceText.text,'NA'],
                                  index=dataFrameColumns), ignore_index=True
                    )
    return xml_data

table = xmldata()
writer = pd.ExcelWriter('output.xlsx')
table.to_excel(writer,'Sheet1')
writer.save()