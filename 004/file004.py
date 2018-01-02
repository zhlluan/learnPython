#filename: 004.py

print('###  using datetime lib  ###')

import datetime
import time
dtstr = input("Enter the datatime(20151215):")
#input default type is string,  str(input(x)) == input(x)
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
another_dtstr = dtstr[:4] + '0101'
#another date is to set month and day to 1, example 20150101
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
print (int((dt-another_dt).days)+1)

print('===  compute by leap year and common year  ===')

runDays  = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
commDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

y = int(input("enter year:"))
m = int(input("enter month:"))
d = int(input("enter day:"))

days = 0

if(m > 12 or m < 1):
    print("Month input error")
    exit(0)

if(d > 31 or d < 1):
	print("Day input error")
	exit(0)

if(y%400 == 0):
    for i in range(0, m-1):
        days += runDays[i]
elif (y%4==0 and y%100!=0):
    for i in range(0, m-1):
        days += runDays[i]
else:
    for i in range(0, m-1):
        days += commDays[i]

days += d

print(days)
