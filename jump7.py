for a in range(1,101):
	b = a//100
	c= (a%100)//10
	d = a%10
		
	if a%7==0 or b == 7 or c == 7 or d == 7:
		continue
	else:
		print(a)