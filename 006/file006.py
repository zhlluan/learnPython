#file 006.py

def F(n):
	if(n==1 or n==2):
	    return 1
	else:
		return (F(n-1) + F(n-2))



n = int(input("input the month:"))
total = F(n);

print("total rabbit number is ", total)
