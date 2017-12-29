#Filename:003.py
print('###  Program 1  ###')

for i in range(0,169):
    for j in range(0,169):
        if (i+j)*(i-j) == 168:
        	print('%d' %((i*i + j*j)/2 - 184))


print('===  Program 2  ===')

import math

x = 1
while True:
	k = x+100
	m = x+100+168
	if ((math.sqrt(k)-int(math.sqrt(k)) == 0) 
	and (math.sqrt(m) - int(math.sqrt(m)) == 0)):
	    print(x)
	    break
	x += 1