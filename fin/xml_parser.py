import  xml.etree.ElementTree as ET

#tree = ET.parse('D:\\Files\\Documents\\Workspace\\Finflock\\Downloads\\Sample_XMLs\\Sample_XMLs\\IBM_Fundamental_Data\\IBM_ReportsFinSummary.xml')
tree = ET.parse('/home/iso-2/Workspace/Finflock/Downloads/Sample_XMLs/Sample_XMLs/IBM_Fundamental_Data/IBM_ReportsFinSummary.xml')

root = tree.getroot()

print('\n\nThe root is :')
print(root.tag)

#print('\n\nAll the attributes of root:')
#print(root.attrib)

print('\n\nThe children nodes are:')
for child in root:
    print(child.tag,child.attrib)

#Add a loop for straight data
#print('\n\nFirst value of the data:')
#print(root[0][0].text)


print('\n\n')
print("############# TotalRevenues ################")
print("\n")
print('\t     asofDate \t\t reportType \t period \t   value '.upper())
print('\t     ======== \t\t ========== \t ====== \t ============= \n')
count = 0
for neighbor in root.iter('TotalRevenue'):
    asofDate = neighbor.attrib['asofDate']
    reportType = neighbor.attrib['reportType']
    period = neighbor.attrib['period']
    value = neighbor.text
    print('\t',count,' ',asofDate,'\t',reportType,'\t\t',period,'\t\t',value)
    count += 1
