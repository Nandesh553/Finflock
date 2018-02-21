from xml_parser_functions import fin_summary



#Enter the path here
#path = 'IBM_Fundamental_Data\\IBM_ReportsFinSummary.xml'
path = 'GOOG_Fundamental_Data\\GOOG_ReportsFinSummary.xml'

#Linux directory
#path = 'IBM_Fundamental_Data/IBM_ReportsFinSummary.xml'
#temp_path = '/home/iso-2/Workspace/Finflock/Downloads/Sample_XMLs/Sample_XMLs/'

temp_path = 'D:\\Files\\Documents\\Workspace\\Finflock\\Downloads\\Sample_XMLs\\'
full_path = temp_path + path



#for Finance_summary
if 'Summary' in path:
	obj = fin_summary(full_path)

	data = obj.main()

	if 'TotalRevenues' in data:
		obj.get_total_revenue()
	if 'ESPs' in data:
		obj.get_esp()
	if 'DividendPerShares' in data:
		obj.dividend_per_share()
	if 'Dividends' in data:
		obj.dividend()
