#!/usr/bin/env python3

import json
from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import timezone

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

f = open('habitdata.txt')
raw = f.read()
# print(raw)
jsond = json.loads(raw)
# print(jsond)

    
habits= []
gooddays =[0,0,0,0,0,0,0,0,0]
baddays =[0,0,0,0,0,0,0,0,0]
	

# output is date, goodday,badday, (habit, 1/0, ...)
# Make a Header record 
output = 'Date'

for habit in jsond:
	habits.insert(0, habit['name'])
	output = output + ', ' + habit['name']

output = output + ', Good Day +1, Good Day +2, Good Day +3,  Good Day +4, Good Day +5, Good Day +6,  Good Day +7 '  
output = output + ', Bad Day +1,  Bad Day +2, Bad Day +3, Bad Day +4, Bad Day +5, Bad Day +6, Bad Day +7 '

print(output)

enddate=date(2015,12,3)
ddate=date.today()
while ddate > enddate:
	ddate=ddate+timedelta(days=-1)
	output = ddate.strftime('%Y-%m-%d')

	goodday = 0
	badday = 0
	
	for habit in jsond:
#		print(habit['name'])
#		output = output + ', ' + habit['name']
		habits.insert(0, habit['name'])
#		print(' dates ')
#		print(habit['completed'])
		testdates = habit['completed']

		doneday = 0
		for testdate in testdates:
			mytestdate = utc_to_local(datetime.strptime(testdate, "%Y-%m-%d %H:%M:%S %z"))
#			print('testdate ' + testdate + ' localdate ' + mytestdate.strftime('%Y-%m-%d'))
			if ddate == mytestdate.date():
				output = output  + ', 1'
				doneday=1
				if habit['name'] == 'Good Day':
					goodday = 1
				if habit['name'] == 'Bad Day':
					badday = 1

		if doneday == 0:
			output = output  + ', 0'
			
	if goodday == 1:
		gooddays.insert(0,1)		
	else:
		gooddays.insert(0,0)
			
	if badday == 1:
		baddays.insert(0,1)		
	else:
		baddays.insert(0,0)
			
	gooddays = gooddays[:8]
	baddays = baddays[:8]
	output = output + ', ' + str(gooddays[1]) + ', ' + str(gooddays[2]) + ', ' + str(gooddays[3]) + ', ' + str(gooddays[4]) + ', ' + str(gooddays[5]) + ', ' + str(gooddays[6]) + ', ' + str(gooddays[7]) 
	output = output + ', ' + str(baddays[1]) + ', ' + str(baddays[2]) + ', ' + str(baddays[3]) + ', ' + str(baddays[4]) + ', ' + str(baddays[5]) + ', ' + str(baddays[6]) + ', ' + str(baddays[7]) 
			
	print(output)

 
#print(habits)
