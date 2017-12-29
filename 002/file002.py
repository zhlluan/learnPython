#Filename:002.py
i = int(input('Enter the profit: '))
array = [1000000, 600000, 400000, 200000, 100000, 0]
rat   = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for index in range(0,6):
    if i > array[index]:
        r += (i - array[index])*rat[index]
        i = array[index]
print('Total reward = ', r)
