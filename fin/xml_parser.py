import  xml.etree.ElementTree as ET

tree = ET.parse('D:\\Files\\Documents\\Workspace\\Finflock\\Downloads\\Sample_XMLs\\Sample_XMLs\\IBM_Fundamental_Data\\IBM_ReportsFinSummary.xml')

root = tree.getroot()

print('\n\nThe root is :')
print(root.tag)

print('\n\nAll the attributes of root:')
print(root.attrib)

print('\n\nThe children nodes are:')
for child in root:
    print(child.tag,child.attrib)

print('\n\nFirst value of the data:')
print(root[0][0].text)


for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
