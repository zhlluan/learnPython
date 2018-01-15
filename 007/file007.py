#Calculate Quadratic Equation

import math

def quadratic(a, b, c):
    if a==0:
        raise TypeError('a should not equal to 0')
    else:
        deta = b*b-4*a*c
        if deta>=0:
            x1=(-b+math.sqrt(deta))/(2*a)
            x2=(-b-math.sqrt(deta))/(2*a)
            return x1,x2
        else:
            raise TypeError('deta < 0, no answer')

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('Test Fail')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('Test Fail')
else:
    print('Test Pass')