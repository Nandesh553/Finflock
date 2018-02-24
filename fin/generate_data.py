from datetime import datetime
import requests

'''
	Author 	:	Nandeshwar Gupta	<guptanandeshwar553@gmail.com>
	Notes 	:	The output file should not be already present.
'''

print('Start Time is: ',datetime.now())

path = 'NYSE.txt'
ticker_path = 'test_xml1.txt'

data_path = 'data.json'

f = open (ticker_path,'r+')

with open(data_path,'a') as fo :
	fo.write('[\n')

for line in f.readlines():

	temp1 = line
	ticker = temp1.split('\t')[0]
	
	#this code fetches the company information.
	flag=1
	while flag < 3:
		try:
			url = 'https://api.iextrading.com/1.0/stock/[]/company'.replace('[]',ticker)
			temp_data = requests.get(url,timeout=20)
			data = temp_data.content.decode('utf-8')
			break
		except Exception as e:
			print('There was an exception')
			print('\t-------Took more time than 20 secs------',e)
			flag += 1
	print('   ================================   ')
	print('\nLine :',temp1)
	print('Ticker:',ticker)
	print('URL   :',url)
	print('DATA  :',data)
	print('\n')

	with open(data_path,'a') as fo :
		fo.write(data)
		fo.write('\n')

with open(data_path,'a') as fo :
	fo.write(']')

print('End Time is  : ',datetime.now())

#print(temp1)
#https://api.iextrading.com/1.0/stock/aapl/company