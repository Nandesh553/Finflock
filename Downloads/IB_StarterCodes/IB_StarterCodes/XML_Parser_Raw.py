import xml.etree.ElementTree as ET
import pandas as pd

print("\n")
print("This is ROOT")
print(root.tag)
print(root.attrib)
print("\n")
print("\n")
print("These are TAGS")
for i in root:
    print(i.tag , i.attrib)
print("\n")
print("###############################################")
print("###############################################")
print("###############################################")
print(root[1].tag , root[0][2].text , root[0][2].attrib)





###  Statements #####
tree = ET.parse('A.xml')
root = tree.getroot()
print("\n\n")
print("Abbr \t Name")
for neighbor in root.iter('mapItem'):
    list_1 = list(neighbor.attrib.values())
    print(list_1[0] , neighbor.text)
print("\n\n")
print("\n\n")
print("Abbr \t Amount")

for neighbor in root.iter('lineItem'):
    list_2 = list(neighbor.attrib.values())
    print(list_2[0] , neighbor.text)
print("\n\n")



## SUMMARY ####
tree = ET.parse('B.xml')
root = tree.getroot()
l = []
df_1 = pd.DataFrame()
print("\n\n")
print("AsofDate \t Report Type \t Period \t EPS")
for neighbor in root.iter('DividendPerShare'):
    list_1 = list(neighbor.attrib.values())
    print(list_1[0],list_1[1] ,list_1[2] ,  neighbor.text)
print("\n\n")
print("\n\n")
print("AsofDate \t Report Type \t Period \t EPS")
for neighbor in root.iter('TotalRevenue'):
    list_2 = list(neighbor.attrib.values())
    print(list_2[0],list_2[1] ,list_2[2] ,  neighbor.text)
print("\n\n")
print("\n\n")
print("AsofDate \t Report Type \t Period \t EPS")
for neighbor in root.iter('EPS'):
    list_3 = list(neighbor.attrib.values())
    print(list_3[0],list_3[1] ,list_3[2] ,   neighbor.text)
print("\n\n")




## OWNERSHIP ######
tree = ET.parse('C.xml')
root = tree.getroot()
a = []
b = []
c = []
d = []
e = []
print("\n\n")

for neighbor in root.iter('Owner'):
    # print(neighbor.attrib.values())
    a.append(list(neighbor.attrib.values()))

for neighbor in root.iter('type'):
    # print(neighbor.text)
    b.append(neighbor.text)

for neighbor in root.iter('name'):
    # print(neighbor.text)
    c.append(neighbor.text)

for neighbor in root.iter('quantity'):
    # print(neighbor.text)
    d.append(neighbor.text)

for neighbor in root.iter('currency'):
    # print(neighbor.text)
    e.append(neighbor.text)
print("OwnerID \t Type \t name \t qunatity \t currency")
for i in range(0,len(a)-1):
    try:
        print(a[i][0] , b[i] , c[i] , d[i] , e[i])
    except:
        print(a[i][0] , b[i] , c[i] , d[i] , "USD")
print("\n\n")
print("\n\n")



###  Snapshots #####
tree = ET.parse('D.xml')
root = tree.getroot()
print("\n\n")
print("Abbr \t Amount")
for neighbor in root.iter('Ratio'):
    list_1 = list(neighbor.attrib.values())
    print(list_1[0] , neighbor.text)
print("\n\n")
print("\n\n")
for neighbor in root.iter('Value'):
    list_1 = list(neighbor.attrib.values())
    print(neighbor.text)

print("\n\n")


### RESC ###
tree = ET.parse('E.xml')
root = tree.getroot()
for i in root:
    print(i.tag , i.text , list(i.attrib.values()))
    for j in i:
        print(j.tag , j.text , list(j.attrib.values()))
        for l in j:
            print(l.tag , l.text , list(l.attrib.values()))
            for m in l:
                print(m.tag , m.text , list(m.attrib.values()))
                for z in m:
                    print(z.tag , z.text , list(z.attrib.values()))
