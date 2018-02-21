import  xml.etree.ElementTree as ET

'''
		Author :	Nandeshwar Gupta
		Notes  :	[DONE]	Make functions for respective codes.
					[TODO]	Reduce code redundancy.
					[DONE]	Check for the data to be present.
'''

#****************************** REPORT FIN SUMMARY **********************************
class fin_summary():

	def __init__(self,path):
		self.path = path
		self.tree = ET.parse(path)


	def main(self):
		#***************Main_function to make some predefined data******************
		print('\n')
		print('############## Fundamental_Data #################')
		tree = self.tree
		root = tree.getroot()
		print('\n\nThe root is :'.upper())
		print(root.tag)
		data = []
		#print('\n\nAll the attributes of root:')
		#print(root.attrib)
		print('\n\nThe children nodes are:'.upper())
		for child in root:
		    print('{}{}'.format(child.tag,child.attrib))
		    data.append(child.tag)
		return data
	#Add a loop for straight data
	#print('\n\nFirst value of the data:')
	#print(root[0][0].text)


	def get_total_revenue(self):
		#*****************This code iterates the TOTAL_REVENUES**********************
		tree = self.tree
		root = tree.getroot()
		print('\n\n')
		print('############### TotalRevenues ##################')
		print('\n')
		print('\t     asofDate \t\t reportType \t period \t value '.upper())
		print('\t     ======== \t\t ========== \t ====== \t ============= \n')
		count = 0
		for neighbor in root.iter('TotalRevenue'):
		    asofDate = neighbor.attrib['asofDate']
		    reportType = neighbor.attrib['reportType']
		    period = neighbor.attrib['period']
		    value = neighbor.text
		    print('\t',count,' ',asofDate,'\t',reportType,'\t\t',period,'\t\t',value)
		    count += 1


	def get_esp(self):
		#*****************This code iterates the EPS's*******************************
		tree = self.tree
		root = tree.getroot()
		print('\n\n')
		print("##################### EPS #######################")
		print('\n')
		print('\t     asofDate \t\t reportType \t period \t value '.upper())
		print('\t     ======== \t\t ========== \t ====== \t ============= \n')
		count = 0
		for neighbor in root.iter('EPS'):
		    asofDate = neighbor.attrib['asofDate']
		    reportType = neighbor.attrib['reportType']
		    period = neighbor.attrib['period']
		    value = neighbor.text
		    print('\t',count,' ',asofDate,'\t',reportType,'\t\t',period,'\t\t',value)
		    count += 1


	def dividend_per_share(self):
		#*****************This code iterates the EPS's*******************************
		tree = self.tree
		root = tree.getroot()
		print('\n\n')
		print("############## DIVIDEND_PER_SHARE ##############")
		print('\n')
		print('\t     asofDate \t\t reportType \t period \t value '.upper())
		print('\t     ======== \t\t ========== \t ====== \t ============= \n')
		count = 0
		for neighbor in root.iter('DividendPerShare'):
		    asofDate = neighbor.attrib['asofDate']
		    reportType = neighbor.attrib['reportType']
		    period = neighbor.attrib['period']
		    value = neighbor.text
		    print('\t',count,' ',asofDate,'\t',reportType,'\t\t',period,'\t\t',value)
		    count += 1

	def dividend(self):
		#*****************This code iterates the EPS's*******************************
		tree = self.tree
		root = tree.getroot()
		print('\n\n')
		print("################# DIVIDEND ##################")
		print('\n')
		print('\ttype   exDate      recordDate   payDate      dec_Date     value'.upper())
		print('\t====   ==========  ==========   ==========   ========     =====\n')
		count = 0
		for neighbor in root.iter('Dividend'):
		    type = neighbor.attrib['type']
		    exDate = neighbor.attrib['exDate']
		    recordDate = neighbor.attrib['recordDate']
		    payDate = neighbor.attrib['payDate']
		    declarationDate = neighbor.attrib['declarationDate']
		    value = neighbor.text
		    print('\t',type,' ',exDate,' ',recordDate,' ',payDate,' ',declarationDate,' ',value)
		    count += 1




class 