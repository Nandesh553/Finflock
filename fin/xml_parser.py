import  xml.etree.ElementTree as ET

tree = ET.parse('D:\\Files\\Documents\\Workspace\\Finflock\\Downloads\\Sample_XMLs\\Sample_XMLs\\IBM_Fundamental_Data\\IBM_ReportsFinSummary.xml')

root = tree.getroot()

print('\nThe root is :')
print(root.tag)

print('\nAll the attributes of root:')
print(root.attrib)

print('\nThe children nodes are:')
for child in root:
    print(child.tag,child.attrib)

print(root[0][1].text)
