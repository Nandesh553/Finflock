import csv
import xlrd
import mmap
import pyodbc as p
import os
import collections
import datetime as dt
import ntpath
import hashlib
import smtplib  # Import smtplib for the actual sending function
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import strftime
# Assign path to Excel files

folder_to_import_csv   = "//vaneck.local/hq/Research/Muni/MuniInventory/BloombergStreetOfferings"
folder_to_import_excel = "//vaneck.local/hq/Research/Muni/MuniInventory/ManualExcelOfferings"
#DateTime configuration - Looking for files that are modified in last twelve hours
now=dt.datetime.now()
ago=now-dt.timedelta(hours=4)

# Database Connection Info
#connStr = "driver={SQL Server};server=PORTFOLIO-LI-01;database=ETFMasterDB;username=ETFUser;password=ETFUser_2013"
connStr = "driver={ODBC Driver 13 for SQL Server};Trusted_Connection=yes;server=finflock.database.windows.net;database=MARKETDATA;username=system.services;password=Finflock123!"
conn = p.connect(connStr)
cursor = conn.cursor()

# Header Row, Only for Information
header_row_version_1 = ['Reference Security', 'Time', 'Src', 'Dealer', 'Name', 'Ask YTW', 'Ask Px', 'Ask Sz', 'Sender Name', 'Sender Firm']
header_row_version_2 = ['Reference Security', 'Time', 'Name', 'Industry', 'State', 'Coupon', 'Maturity', 'Ask YTW', 'Ask Sz', 'Ask Px', 'Maturity Type', 'Tax Provision', 'Pre-Re Mat', 'Sender Firm', 'Sender Name']
# Excel Header Row, Only for information
excel_header_version_1 = ['MLNO','Cusip','Description','Amount','MLUAYield','MLUAPrice','State','Coupon','Maturity','Moody','SandP','EvalPrice','Insurer','NextCallDate','RefundDate','Features','Source','MinOffer','IncrOffer']
excel_header_version_2 = ['CUSIP', 'Quantity']

# Email Server 
emailHost = 'wmail.vaneck.com'
# Email Settings
msg = MIMEMultipart('alternative')
msg['Subject'] = "[FI Quant] uploaded files into Database Successfully"
msg['From'] = "srinath@finflock.com"

msg['To'] = "srinath@finflock.com"
html = """\
<html>
    <head></head>
    <body>
        <p>Success<br>
             Inventory Files are loaded from - G:\Muni\MuniInventory\BloombergStreetOfferings\Bloomberg*.csv (last modified in 4 hours)<br>
                                             - G:\Muni\MuniInventory\BloombergStreetOfferings\Munis_Market*.csv (last modified in 4 hours)<br>
                                             - G:\Muni\MuniInventory\ManualExcelOfferings\*.xlsx (last modified in 4 hours)<br>
             Securities are loaded into MuniInventory table in ETFMasterDB
        </p>
    </body>
</html>
"""


### Regular Expressions for Yield, Price, Size ####
Cusip_Keys  = ['Cusip','Reference Key','Reference Security','CUSIP']
Amount_Keys = ['Amount','Ask Sz','Ask Size', 'Quantity','O Size', 'PAR', 'Offer Qty']
Price_Keys  = ['Ask Px', 'Ask Price', 'Ask Prc', 'Price', 'Px', 'MLUAPrice', 'IDC Eval. Bid', 'IDC Eval. Mean','O Price','Ofr Px']
Yield_Keys  = ['MLUAYield','Ask YTW','Ask Yield To Worst', 'Yield to Worst', 'Yield','O Yield','Ofr YTW']
Source_Keys = ['Src','Name', 'Description', 'Short Name']
Sender_Firm = ['Sender Firm', 'Firm', 'Source','O Source']
Sender_Name = ['Sender Name']
Dealer_Keys = ['Dealer','Insurer']

Call_Date_Keys = ['Call Date']
Call_Price_Keys = ['Call Price']
Call_Type_Keys = ['Call Type']
AMT_Keys = ['AMT']
Ratings_Keys = ['Ratings']
IDC_Price_Keys = ['IDC Price']
IDC_Yield_Keys = ['IDC Yield']
SPSE_Price_Keys = ['SPSE Price']
SPSE_Yield_Keys = ['SPSE Yield']

### FUnction for XLS Dict Reader
try:
    def XLSDictReader(excel_file, sheet_index=0):
        f = open(excel_file, 'rb')
        data    = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        book    = xlrd.open_workbook(file_contents=data)
        sheet   = book.sheet_by_index(sheet_index)
    
        def item(i, j):
            return (sheet.cell_value(0,j), sheet.cell_value(i,j))

        return ( dict(item(i,j) for j in range(sheet.ncols)) \
                     for i in range(1, sheet.nrows) )

except ImportError:
    XLSDictReader = None


print "Time of Load:" + strftime("%Y-%m-%d %H:%M:%S")
print ""
### Delete previous files from Inventory for todays load
#cursor.execute("DELETE FROM MuniInventory where dtLoadDate >= CONVERT (date, GETDATE())")
#print "Deleted todays Inventory Load if there were any loaded"
cursor.execute("DELETE FROM MuniInventory")
print "Deleted todays Inventory Load if there were any loaded"
                
### CSV Files to Download
csv_files_to_import = os.listdir(folder_to_import_csv)
for file_to_import in csv_files_to_import:
        if file_to_import.startswith('Bloomberg') and file_to_import.endswith('.csv'):
            csv_fileName = os.path.join(folder_to_import_csv, file_to_import)
            st=os.stat(csv_fileName)    
            mtime=dt.datetime.fromtimestamp(st.st_mtime)
            if mtime>ago:
                print "\nReading csv File: "+csv_fileName
                csv_data = csv.DictReader(file(csv_fileName),dialect='excel', delimiter=',')
                rows_list = []
                for row in csv_data:
                    d = collections.OrderedDict()
                    for key in row:
                        if key.lower() in [x.lower() for x in Price_Keys]:
                            d['Price'] = row[key]
                        if key.lower() in [x.lower() for x in Amount_Keys]:
                            d['Amount'] = row[key]
                        if key.lower() in [x.lower() for x in Yield_Keys]:
                            d['Yield'] = row[key]    
                        if key.lower() in [x.lower() for x in Cusip_Keys]:
                            d['Cusip'] = row[key] 
                        if key.lower() in [x.lower() for x in Source_Keys]:
                            d['Source'] = row[key] 
                        if key.lower() in [x.lower() for x in Sender_Firm]:
                            d['SenderFirm'] = row[key] 
                        if key.lower() in [x.lower() for x in Sender_Name]:
                            d['SenderName'] = row[key]      
                        #if key.lower() in [x.lower() for x in Dealer_Keys]:
                        #    d['Dealer'] = row[key]             
                        d['FileName'] =  csv_fileName
                        #print d
                        
                    if 'Price' not in d:
                        d['Price'] = '9999.0'
                    if 'Amount' not in d or d['Amount']=='':
                        d['Amount'] = '-99.0'
                    if 'Yield' not in d or d['Yield']=='':
                        d['Yield'] = '-99.0'
                    if 'Cusip' not in d:
                        d['Cusip'] = ''
                    if 'Source' not in d:
                        d['Source'] = ntpath.basename(csv_fileName)
                    if 'SenderName' not in d:
                        d['SenderName'] = ntpath.basename(csv_fileName)    
                    if 'SenderFirm' not in d:
                        d['SenderFirm'] = ntpath.basename(csv_fileName)
                    rows_list.append(d)   
                
                for row in rows_list:
                    try:
                        if row['Cusip'] and str(row['Cusip']).strip(): 
                            cursor.execute("INSERT INTO MuniInventory(sRefSecurity,sAskYTW,sAskPx,sAskSize,sFileName,sSource, sSenderName, sSenderFirm)" "VALUES (?, ?, ?, ?, ?,?,?,?)", (row['Cusip'],row['Yield'],row['Price'],row['Amount'],row['FileName'],row['Source'],row['SenderName'], row['SenderFirm']))
                        #cursor.execute("INSERT INTO MuniInventory_History(sRefSecurity,sAskYTW,sAskPx,sAskSize,sFileName,sSource, sSenderName, sSenderFirm)" "VALUES (?, ?, ?, ?, ?,?,?,?)", (row['Cusip'],row['Yield'],row['Price'],row['Amount'],row['FileName'],row['Source'],row['SenderName'],row['SenderFirm']))
                    except (RuntimeError, TypeError, NameError, ValueError):
                        pass        
                print "Loading csv File COMPLETE: "+csv_fileName

        if file_to_import.startswith('MKTX') and file_to_import.endswith('.csv'):
            csv_fileName0 = os.path.join(folder_to_import_csv, file_to_import)
            lines = open(csv_fileName0).readlines()
            open(os.path.join(folder_to_import_csv, 'MKTX_Modified.csv'), 'w').writelines(lines[6:-1])
            csv_fileName = os.path.join(folder_to_import_csv, 'MKTX_Modified.csv')
            st=os.stat(csv_fileName0)    
            mtime=dt.datetime.fromtimestamp(st.st_mtime)
            if mtime>ago:
                print "\nReading csv File: "+csv_fileName0
                csv_data = csv.DictReader(file(csv_fileName),dialect='excel', delimiter=',')
                rows_list = []
                for row in csv_data:
                    d = collections.OrderedDict()
                    for key in row:
                        if key.lower() in [x.lower() for x in Price_Keys]:
                            d['Price'] = row[key].replace('N/A','').replace(',','')
                        if key.lower() in [x.lower() for x in Amount_Keys]:
                            d['Amount'] = row[key].replace(',','').replace('N/A','')
                            d['Amount'] += '000'
                        if key.lower() in [x.lower() for x in Yield_Keys]:
                            d['Yield'] = row[key].replace('N/A','')    
                        if key.lower() in [x.lower() for x in Cusip_Keys]:
                            d['Cusip'] = row[key] 
                        if key.lower() in [x.lower() for x in Source_Keys]:
                            d['Source'] = row[key] 
                        if key.lower() in [x.lower() for x in Sender_Firm]:
                            d['SenderFirm']= row[key]
                        if key.lower() in [x.lower() for x in Sender_Name]:
                            d['SenderName'] = row[key]
                        ###################################################
                        if key.lower() in [x.lower() for x in Call_Date_Keys]:
                            d['Call_Date'] = row[key]        
                        if key.lower() in [x.lower() for x in Call_Price_Keys ]:
                            d['Call_Price'] = row[key]  
                        if key.lower() in [x.lower() for x in Call_Type_Keys ]:
                            d['Call_Type'] = row[key]  
                        if key.lower() in [x.lower() for x in AMT_Keys ]:
                            d['AMT'] = row[key]  
                        if key.lower() in [x.lower() for x in Ratings_Keys ]:
                            d['Ratings'] = row[key]  
                        if key.lower() in [x.lower() for x in IDC_Price_Keys ]:
                            d['IDC_Price'] = row[key]  
                        if key.lower() in [x.lower() for x in IDC_Yield_Keys ]:
                            d['IDC_Yield'] = row[key]  
                        if key.lower() in [x.lower() for x in SPSE_Price_Keys ]:
                            d['SPSE_Price'] = row[key]  
                        if key.lower() in [x.lower() for x in SPSE_Yield_Keys ]:
                            d['SPSE_Yield'] = row[key]      
                        #if key.lower() in [x.lower() for x in Dealer_Keys]:
                        #    d['Dealer'] = row[key]             
                        d['FileName'] =  csv_fileName
                        #print d
                       
                    if 'Price' not in d:
                        d['Price'] = '9999.0'
                    if 'Amount' not in d or d['Amount']=='':
                        d['Amount'] = '-99.0'
                    if 'Yield' not in d or d['Yield']=='':
                        d['Yield'] = '-99.0'
                    if 'Cusip' not in d:
                        d['Cusip'] = ''
                    if 'Source' not in d:
                        d['Source'] = ntpath.basename(csv_fileName)
                    if 'SenderFirm' not in d:
                        d['SenderFirm'] = ntpath.basename(csv_fileName)
                    if 'SenderName' not in d:
                        d['SenderName'] = ntpath.basename(csv_fileName)
                   
                       
                    
                    rows_list.append(d)   
                
                for row in rows_list:
                    try:
                        if row['Cusip'] and str(row['Cusip']).strip():
                        #print 'Cusip:' + row['Cusip']
                            cursor.execute("INSERT INTO MuniInventory(sRefSecurity, sAskYTW, sAskPx, sAskSize, sSource, sSenderName, sSenderFirm, sCallDate, sCallPrice, sCallType, sAMT, sRatings, sIDCPrice, sIDCYield, sSPSEPrice, sSPSEYield, sFileName)" "VALUES (?, ?, ?, ?, ?,?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row['Cusip'],row['Yield'],row['Price'],float(row['Amount']),row['Source'], row['SenderName'], row['SenderFirm'], row['Call_Date'], row['Call_Price'], row['Call_Type'], row['AMT'], row['Ratings'], row['IDC_Price'], row['IDC_Yield'], row['SPSE_Price'], row['SPSE_Yield'], row['FileName']))
                    except (RuntimeError, TypeError, NameError, ValueError):
                        pass    
                print "Loading csv File COMPLETE: "+csv_fileName0
         
        if file_to_import.startswith('tmcreport') and file_to_import.endswith('.csv'):
            csv_fileName0 = os.path.join(folder_to_import_csv, file_to_import)
            lines = open(csv_fileName0).readlines()
            open(os.path.join(folder_to_import_csv, 'tmcreport_Modified.csv'), 'w').writelines(lines[2:-1])
            csv_fileName = os.path.join(folder_to_import_csv, 'tmcreport_Modified.csv')
            st=os.stat(csv_fileName0)    
            mtime=dt.datetime.fromtimestamp(st.st_mtime)
            if mtime>ago:
                print "\nReading csv File: "+csv_fileName0
                csv_data = csv.DictReader(file(csv_fileName),dialect='excel', delimiter=',')
                rows_list = []
                for row in csv_data:
                    d = collections.OrderedDict()
                    for key in row:
                        if key.lower() in [x.lower() for x in Price_Keys]:
                            d['Price'] = row[key].replace('N/A','').replace(',','')
                        if key.lower() in [x.lower() for x in Amount_Keys]:
                            d['Amount'] = row[key].replace(',','').replace('N/A','')
                            d['Amount'] += '000'
                        if key.lower() in [x.lower() for x in Yield_Keys]:
                            d['Yield'] = row[key].replace('N/A','')    
                        if key.lower() in [x.lower() for x in Cusip_Keys]:
                            d['Cusip'] = row[key] 
                        if key.lower() in [x.lower() for x in Source_Keys]:
                            d['Source'] = csv_fileName0#row[key] 
                        if key.lower() in [x.lower() for x in Sender_Firm]:
                            d['SenderFirm']= 'TMC'#row[key]
                        if key.lower() in [x.lower() for x in Sender_Name]:
                            d['SenderName'] = 'TMC'#row[key]
                        ###################################################
                        d['FileName'] =  csv_fileName0
                        #print d
                       
                    if 'Price' not in d:
                        d['Price'] = '9999.0'
                    if 'Amount' not in d or d['Amount']=='':
                        d['Amount'] = '-99.0'
                    if 'Yield' not in d or d['Yield']=='':
                        d['Yield'] = '-99.0'
                    if 'Cusip' not in d:
                        d['Cusip'] = ''
                    if 'Source' not in d:
                        d['Source'] = ntpath.basename(csv_fileName0)
                    if 'SenderFirm' not in d:
                        d['SenderFirm'] = ntpath.basename(csv_fileName0)
                    if 'SenderName' not in d:
                        d['SenderName'] = ntpath.basename(csv_fileName0)
                   
                       
                    
                    rows_list.append(d)   
                
                for row in rows_list:
                    try:
                        if row['Cusip'] and str(row['Cusip']).strip(): 
                            cursor.execute("INSERT INTO MuniInventory(sRefSecurity,sAskYTW,sAskPx,sAskSize,sFileName,sSource, sSenderName, sSenderFirm)" "VALUES (?, ?, ?, ?, ?,?,?,?)", (row['Cusip'],row['Yield'],row['Price'],row['Amount'],row['FileName'],row['Source'],row['SenderName'], row['SenderFirm']))
                    except (RuntimeError, TypeError, NameError, ValueError):
                        pass    
                print "Loading csv File COMPLETE: "+csv_fileName0
                
### Excel Files to Download
excel_files_to_import = os.listdir(folder_to_import_excel)
for file_to_import in excel_files_to_import:
        if file_to_import.endswith('.xlsx') or file_to_import.endswith('.xls'):
            excel_file = os.path.join(folder_to_import_excel, file_to_import)
            st=os.stat(excel_file)    
            mtime=dt.datetime.fromtimestamp(st.st_mtime)
            if mtime>ago:
                print "\nReading excel File: "+excel_file
                excel_DictData = XLSDictReader(excel_file)
                rows_list = []
                for row in excel_DictData:
                    d = collections.OrderedDict()
                    for key in row:
                        print (row[key])
                        #print "key:", key
                        #for  x in Price_Keys:
                        #    print "Type:", x, " - " , type(x)
                        if key.lower() in [x.lower() for x in Price_Keys]:
                            d['Price'] = row[key]
                        if key.lower() in [x.lower() for x in Amount_Keys]:
                            d['Amount'] = row[key]
                        if key.lower() in [x.lower() for x in Yield_Keys]:
                            d['Yield'] = row[key]    
                        if key.lower() in [x.lower() for x in Cusip_Keys]:
                            if (type(row[key]) == str):
                                d['Cusip'] = str(row[key].strip())
                            else:
                                d['Cusip'] = (row[key])
                        if key.lower() in [x.lower() for x in Source_Keys]:
                            d['Source'] = row[key] 
                        if key.lower() in [x.lower() for x in Sender_Firm]:
                            d['SenderFirm'] = row[key] 
                        if key.lower() in [x.lower() for x in Sender_Name]:
                            d['SenderName'] = row[key]      
                        #if key.lower() in [x.lower() for x in Dealer_Keys]:
                        #    d['Dealer'] = row[key]
                        d['FileName'] =  excel_file

                    if 'Price' not in d:
                        d['Price'] = '9999.0'
                    if 'Amount' not in d:
                        d['Amount'] = '-99.0'
                    if 'Yield' not in d:
                        d['Yield'] = '-99.0'
                    if 'Cusip' not in d:
                        d['Cusip'] = ''
                    if 'Source' not in d:
                        d['Source'] = ntpath.basename(excel_file)
                    if 'SenderFirm' not in d:
                        d['SenderFirm'] = ntpath.basename(excel_file)
                    if 'SenderName' not in d:
                        d['SenderName'] = ntpath.basename(excel_file)
                            
                    rows_list.append(d)  

                for row in rows_list:
                    try:
                        #print ("Cusip:" + row['Cusip'])
                        if row['Cusip'] and str(row['Cusip']).strip():
                            cursor.execute("INSERT INTO MuniInventory(sRefSecurity,sAskYTW,sAskPx,sAskSize,sFileName,sSource, sSenderName, sSenderFirm)" "VALUES (?, ?, ?, ?, ?,?,?,?)", (row['Cusip'],row['Yield'],row['Price'],float(row['Amount']),row['FileName'],row['Source'],row['SenderName'],row['SenderFirm']))
                    except (RuntimeError, TypeError, NameError, ValueError):
                        pass    
                print "Loading Excel File COMPLETE: "+excel_file 
                #print rows_list           


cursor.execute("insert into dbo.MuniInventory_History (dtLoadDate,sRefSecurity,sTime,sSource,sDealer,sName,sAskYTW,sAskPx,sAskSize,sSenderName,sSenderFirm,sCreateUser,dtCreateDate,sIndustry,sState,sCoupon,sMaturity,sMaturityType,sTaxProvision,sPreReMat,sFileName, sCallDate, sCallPrice, sCallType, sAMT, sRatings, sIDCPrice, sIDCYield, sSPSEPrice, sSPSEYield) select dtLoadDate,sRefSecurity,sTime,sSource,sDealer,sName,sAskYTW,sAskPx,sAskSize,sSenderName,sSenderFirm,sCreateUser,dtCreateDate,sIndustry,sState,sCoupon,sMaturity,sMaturityType,sTaxProvision,sPreReMat,sFileName, sCallDate, sCallPrice, sCallType, sAMT, sRatings, sIDCPrice, sIDCYield, sSPSEPrice, sSPSEYield from [dbo].[MuniInventory]")
print "Loading snapshot into History Inventory Tables COMPLETE: "     


cursor.close()
conn.commit()
conn.close()

print "\n\nInventory Files are successfully loaded into Database!"




# Send Email
# Record the MIME types of both parts - text/plain and text/html.
part = MIMEText(html, 'html')
msg.attach(part)
s = smtplib.SMTP(emailHost)
s.sendmail(msg['From'], msg['To'], msg.as_string()) # sendmail function takes 3 arguments: sender's address, recipient's address and message to send - here it is sent as one string.
s.quit()
print 'Email sent successfully!'

