import xml.etree.ElementTree as ET
tree = ET.parse('D:\\Files\\Documents\\Workspace\\Finflock\\Downloads\\Sample_XMLs\\Sample_XMLs\\IBM_Fundamental_Data\\IBM_ReportsFinStatements.xml')
root = tree.getroot()
values= []
for CoIDs in root.findall('CoIDs'):
    coid = CoIDs.findall('CoID')

for i in range(len(coid)):
    print(coid[i].text)



print(root)
