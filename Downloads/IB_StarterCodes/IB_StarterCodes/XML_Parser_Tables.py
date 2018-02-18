# ▀▄▒▄▀ ▒█▀▄▀█ ▒█░░░ 　 ▒█▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀█
# ░▒█░░ ▒█▒█▒█ ▒█░░░ 　 ▒█▄▄█ █▄▄█ █▄▄▀ ▀▀█ █▀▀ █▄▄▀
# ▄▀▒▀▄ ▒█░░▒█ ▒█▄▄█ 　 ▒█░░░ ▀░░▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀░▀▀


import xml.etree.ElementTree as ET
import pandas as pd


### USEFUL DATA

# print("\n")
# print("ROOT")
# print(root.tag)
# print(root.attrib)
# print("\n")
# print("\n")
# print("All TAGS")
# for i in root:
#     print(i.tag , i.attrib)
# print("\n")
# print("###############################################")
# print("###############################################")
# print("###############################################")
# print(root[1].tag , root[0][2].text , root[0][2].attrib)





# ▒█▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 　 ▒█▀▀▀ ░▀░ █▀▀▄ ▒█▀▀▀█ ▀▀█▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀
# ▒█▄▄▀ █▀▀ █░░█ █░░█ █▄▄▀ ░░█░░ ▀▀█ 　 ▒█▀▀▀ ▀█▀ █░░█ ░▀▀▀▄▄ ░░█░░ █▄▄█ ░░█░░ █▀▀ █░▀░█ █▀▀ █░░█ ░░█░░ ▀▀█
# ▒█░▒█ ▀▀▀ █▀▀▀ ▀▀▀▀ ▀░▀▀ ░░▀░░ ▀▀▀ 　 ▒█░░░ ▀▀▀ ▀░░▀ ▒█▄▄▄█ ░░▀░░ ▀░░▀ ░░▀░░ ▀▀▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀

tree = ET.parse('D:\\Files\\Documents\\Workspace\\Finflock\\Downloads\\Sample_XMLs\\Sample_XMLs\\IBM_Fundamental_Data\\IBM_ReportsFinStatements.xml')
root = tree.getroot()
df_MapItem_Table = pd.DataFrame()
df_Balance_Sheet = pd.DataFrame()
print("\n\n")
print("############# Map_Item_Table ################")
print("\n")
for neighbor in root.iter('mapItem'):
    list_1 = list(neighbor.attrib.values())
    Name  = str(neighbor.text)
    list_1.append(Name)
    temp = pd.DataFrame([list_1])
    df_MapItem_Table = df_MapItem_Table.append(temp)
print("\n\n")
df_MapItem_Table.columns = ['coaItem', 'statementType' , 'lineID' , 'precision' , 'Item_Name']
print(df_MapItem_Table.head())
print("\n")
print("Total Values\t:\t" , df_MapItem_Table.shape)
print("\n\n")
count = 0
for i in root:
    for j in i:
        for k in j:
            for l in k:
                for m in l:
                    list_1 = list(m.attrib.values())
                    # Amt  = float(m.text)
                    list_1.append(m.text)
                    temp = pd.DataFrame([list_1])
                    df_Balance_Sheet = df_Balance_Sheet.append(temp)
                print("\n\n")
                print("############# BalanceSheet" ,count , " ################")
                df_Balance_Sheet.columns = ['coaCode', 'Value']
                print(df_Balance_Sheet.head())
                print("\n")
                print("Total Values\t:\t" , df_Balance_Sheet.shape)
                print("\n\n")
                df_Balance_Sheet = pd.DataFrame()
                count = count + 1




# ▒█▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 　 ▒█▀▀▀ ░▀░ █▀▀▄ ▒█▀▀▀█ █░░█ █▀▄▀█ █▀▄▀█ █▀▀█ █▀▀█ █░░█
# ▒█▄▄▀ █▀▀ █░░█ █░░█ █▄▄▀ ░░█░░ ▀▀█ 　 ▒█▀▀▀ ▀█▀ █░░█ ░▀▀▀▄▄ █░░█ █░▀░█ █░▀░█ █▄▄█ █▄▄▀ █▄▄█
# ▒█░▒█ ▀▀▀ █▀▀▀ ▀▀▀▀ ▀░▀▀ ░░▀░░ ▀▀▀ 　 ▒█░░░ ▀▀▀ ▀░░▀ ▒█▄▄▄█ ░▀▀▀ ▀░░░▀ ▀░░░▀ ▀░░▀ ▀░▀▀ ▄▄▄█

df_DividendPerShare = pd.DataFrame()
df_TotalRevenue = pd.DataFrame()
df_EPS = pd.DataFrame()
df_Dividend = pd.DataFrame()

tree = ET.parse('ReportsFinSummary.xml')
root = tree.getroot()
print("\n\n")
print("############# DividendPerShare ################")
print("\n")
for neighbor in root.iter('DividendPerShare'):
    list_1 = list(neighbor.attrib.values())
    Amt  = float(neighbor.text)
    list_1.append(Amt)
    temp = pd.DataFrame([list_1])
    df_DividendPerShare = df_DividendPerShare.append(temp)
df_DividendPerShare.columns = ['AsofDate', 'Report_Type' , 'Period' , 'DividendPerShare']
print(df_DividendPerShare.head())

print("\n")
print("Total Values\t:\t" , df_DividendPerShare.shape)
print("\n\n")
print("\n\n")
print("############# TotalRevenue ################")
print("\n")

for neighbor in root.iter('TotalRevenue'):
    list_2 = list(neighbor.attrib.values())
    Amt  = float(neighbor.text)
    list_2.append(Amt)
    temp = pd.DataFrame([list_2])
    df_TotalRevenue = df_TotalRevenue.append(temp)
df_TotalRevenue.columns = ['AsofDate', 'Report_Type' , 'Period' , 'TotalRevenue']
print(df_TotalRevenue.head())

print("\n")
print("Total Values\t:\t" , df_TotalRevenue.shape)
print("\n\n")
print("\n\n")
print("############# EPS ################")
print("\n")

for neighbor in root.iter('EPS'):
    list_3 = list(neighbor.attrib.values())
    Amt  = float(neighbor.text)
    list_3.append(Amt)
    temp = pd.DataFrame([list_3])
    df_EPS = df_EPS.append(temp)
df_EPS.columns = ['AsofDate', 'Report_Type' , 'Period' , 'EPS']
print(df_EPS.head())

print("\n")
print("Total Values\t:\t" , df_EPS.shape)
print("\n\n")
print("\n\n")
print("############# Dividend ################")
print("\n")

for neighbor in root.iter('Dividend'):
    list_4 = list(neighbor.attrib.values())
    Amt  = float(neighbor.text)
    list_4.append(Amt)
    temp = pd.DataFrame([list_4])
    df_Dividend = df_Dividend.append(temp)
df_Dividend.columns = ['type', 'exDate' , 'recordDate' , 'payDate' , 'declarationDate' , 'Dividend']
print(df_Dividend.head())

print("\n")
print("Total Values\t:\t" , df_Dividend.shape)
print("\n\n")




# ▒█▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 　 ▒█▀▀▀█ █░░░█ █▀▀▄ █▀▀ █▀▀█ █▀▀ █░░█ ░▀░ █▀▀█
# ▒█▄▄▀ █▀▀ █░░█ █░░█ █▄▄▀ ░░█░░ ▀▀█ 　 ▒█░░▒█ █▄█▄█ █░░█ █▀▀ █▄▄▀ ▀▀█ █▀▀█ ▀█▀ █░░█
# ▒█░▒█ ▀▀▀ █▀▀▀ ▀▀▀▀ ▀░▀▀ ░░▀░░ ▀▀▀ 　 ▒█▄▄▄█ ░▀░▀░ ▀░░▀ ▀▀▀ ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀ █▀▀▀

tree = ET.parse('ReportsOwnership.xml')
root = tree.getroot()
a = []
b = []
c = []
d = []
e = []
df_Ownership = pd.DataFrame()
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
# print("OwnerID \t Type \t name \t qunatity \t currency")
for i in range(0,len(a)-1):
    try:
        # print(a[i][0] , b[i] , c[i] , d[i] , e[i])
        list_1 = [a[i][0] , b[i] , c[i] , d[i] , e[i]]
        temp = pd.DataFrame([list_1])
        df_Ownership = df_Ownership.append(temp)

    except:
        # print(a[i][0] , b[i] , c[i] , d[i] , "USD")
        list_2 = [a[i][0] , b[i] , c[i] , d[i] , "USD"]
        temp = pd.DataFrame([list_2])
        df_Ownership = df_Ownership.append(temp)
print("\n\n")
print("############# OwnerShip ################")
print("\n")
df_Ownership.columns = ['OwnerID', 'Type' , 'Name' , 'Quantity' , 'Currency']
print(df_Ownership.head())
print("\n")
print("Total Values\t:\t" , df_Ownership.shape)
print("\n\n")
print("\n\n")



# ▒█▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ 　 ▒█▀▀▀█ █▀▀▄ █▀▀█ █▀▀█ █▀▀ █░░█ █▀▀█ ▀▀█▀▀
# ▒█▄▄▀ █▀▀ █░░█ █░░█ █▄▄▀ ░░█░░ 　 ░▀▀▀▄▄ █░░█ █▄▄█ █░░█ ▀▀█ █▀▀█ █░░█ ░░█░░
# ▒█░▒█ ▀▀▀ █▀▀▀ ▀▀▀▀ ▀░▀▀ ░░▀░░ 　 ▒█▄▄▄█ ▀░░▀ ▀░░▀ █▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀▀ ░░▀░░

tree = ET.parse('ReportSnapshot.xml')
root = tree.getroot()
df_TextSummary = pd.DataFrame()
df_IndustryInfo = pd.DataFrame()
df_Ratios = pd.DataFrame()
df_Officer_List_1 = pd.DataFrame()
df_Officer_List_2 = pd.DataFrame()
df_Officer_List_3 = pd.DataFrame()
df_Officer_List_4 = pd.DataFrame()
df_Officer_List_5 = pd.DataFrame()
print("\n\n")
print("\n\n")
print("############# Text_Summary ################")
print("\n")
for neighbor in root.iter('Text'):
    list_1 = list(neighbor.attrib.values())
    Amt  = str(neighbor.text)
    list_1.append(Amt)
    temp = pd.DataFrame([list_1])
    df_TextSummary = df_TextSummary.append(temp)
df_TextSummary.columns = ['Type', 'LastModified' , 'Summary']
print(df_TextSummary.head())
print("\n")
print("Total Values\t:\t" , df_TextSummary.shape)
print("\n\n")
print("\n\n")
print("############# Industry_Mapping ################")
print("\n")
for neighbor in root.iter('Industry'):
    list_2 = list(neighbor.attrib.values())
    Amt  = str(neighbor.text)
    list_2.append(Amt)
    temp = pd.DataFrame([list_2])
    df_IndustryInfo = df_IndustryInfo.append(temp)
df_IndustryInfo.columns = ['Type', 'Order' , 'Reported' , 'Code' , 'Mnem' , 'Industry']
print(df_IndustryInfo.head())
print("\n")
print("Total Values\t:\t" , df_IndustryInfo.shape)
print("\n\n")
print("\n\n")
print("############# Ratios ################")
print("\n")
for neighbor in root.iter('Ratio'):
    list_3 = list(neighbor.attrib.values())
    Amt  = str(neighbor.text)
    list_3.append(Amt)
    temp = pd.DataFrame([list_3])
    df_Ratios = df_Ratios.append(temp)
df_Ratios.columns = ['FieldName', 'Type' , 'Value']
print(df_Ratios.head())
print("\n")
print("Total Values\t:\t" , df_Ratios.shape)
print("\n\n")

for neighbor in root.iter('officer'):
    list_3 = list(neighbor.attrib.values())
    Amt  = str(neighbor.text)
    # list_3.append(Amt)
    temp = pd.DataFrame([list_3])
    df_Officer_List_1 = df_Officer_List_1.append(temp)
df_Officer_List_1.columns = ['Rank', 'Since']


for neighbor in root.iter('firstName'):
    list_3 = []
    Amt  = str(neighbor.text)
    list_3.append(Amt)
    temp = pd.DataFrame([list_3])
    df_Officer_List_2 = df_Officer_List_2.append(temp)
df_Officer_List_2.columns = ['First_Name']

for neighbor in root.iter('lastName'):
    list_3 = []
    Amt  = str(neighbor.text)
    list_3.append(Amt)
    temp = pd.DataFrame([list_3])
    df_Officer_List_3 = df_Officer_List_3.append(temp)
df_Officer_List_3.columns = ['Last_Name']


for neighbor in root.iter('age'):
    list_3 = []
    Amt  = str(neighbor.text)
    list_3.append(Amt)
    temp = pd.DataFrame([list_3])
    df_Officer_List_4 = df_Officer_List_4.append(temp)
df_Officer_List_4.columns = ['Age']


for neighbor in root.iter('title'):
    list_3 = []
    Amt  = str(neighbor.text)
    list_3.append(Amt)
    temp = pd.DataFrame([list_3])
    df_Officer_List_5 = df_Officer_List_5.append(temp)
df_Officer_List_5.columns = ['Title']

print("\n\n")
print("############# Officers_List ################")
print("\n")
result = pd.concat([df_Officer_List_1 , df_Officer_List_2 , df_Officer_List_3 , df_Officer_List_4, df_Officer_List_5], axis=1, join='inner')
print(result.head())



# ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▀█ ▒█▀▀█
# ▒█▄▄▀ ▒█▀▀▀ ░▀▀▀▄▄ ▒█░░░
# ▒█░▒█ ▒█▄▄▄ ▒█▄▄▄█ ▒█▄▄█

tree = ET.parse('RESC.xml')
root = tree.getroot()
# # for neighbor in root.iter('FYPeriod'):
# #     list_1 = list(neighbor.attrib.values())
# #     print(list_1[0] , neighbor.text)
print("\n\n")
print("############# Cons_Estimate ################")
print("\n")
df_ConsEstimate = pd.DataFrame()
for neighbor in root.iter('ConsValue'):
    list_4 = list(neighbor.attrib.values())
    Amt  = str(neighbor.text)
    list_4.append(Amt)
    temp = pd.DataFrame([list_4])
    df_ConsEstimate = df_ConsEstimate.append(temp)
df_ConsEstimate.columns = ['Date_Type', 'Value']
print(df_ConsEstimate.head())

print("\n")
print("Total Values\t:\t" , df_ConsEstimate.shape)
print("\n\n")
