import sys
import pandas as pd
from datetime import datetime

#functions
def is_exist(item, clients):
	index = 0
	for client in clients:
		if (item.date() == client[0].date()):
			return index
		index = index + 1
	return -1

#read input command
inputfile = None
outputfile = None
fromdate = None
todate = None
onlyvalue = False

for index, item in enumerate(sys.argv):
	if(sys.argv[index] == '-i'):
		inputfile = sys.argv[index+1]
	elif(sys.argv[index] == '-o'):
		outputfile = sys.argv[index+1]
	elif(sys.argv[index] == '-f'):
		fromdate = sys.argv[index+1]
	elif(sys.argv[index] == '-t'):
		todate = sys.argv[index+1]
	elif(sys.argv[index] == '-p'):		
		onlyvalue = True if (sys.argv[index+1] == 'T') else False
		
#validate input arguments
if(inputfile is None):
	print('Fail: Input file not found.')
	sys.exit()
if(outputfile is None):
	print('Fail: Output file not found.')
	sys.exit()
		
#read files
with open(inputfile) as f:
	lines = f.read().splitlines()
dataset = [line.split('\t') for line in lines]

#convert to date object
for item in dataset:
	item[0] = datetime.strptime(item[0], '%Y-%m-%d')

#create date list of the time series
if(fromdate is not None):
	date1 = datetime.strptime(fromdate, '%Y-%m-%d')
else:
	date1 = dataset[0][0]

if(todate is not None):
	date2 = datetime.strptime(todate, '%Y-%m-%d')
else:
	date2 = datetime.now()

date_series = pd.date_range(date1, date2).tolist()

#Process
processed_result = []
for idate in date_series:
	index = is_exist(idate, dataset)
	if(index > -1):
		processed_result.append([idate, dataset[index][1]])
	else:
		processed_result.append([idate, 0])
		
#write files
with open(outputfile,'w') as f1:
	if(onlyvalue):
		for item in processed_result:
			f1.write(str(item[1]) + "\n")
	else:
		for item in processed_result:
			f1.write(str(item[0].date()) + "\t" + str(item[1]) + "\n")
		
print('Completed.')