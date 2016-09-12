###### this is the second .py file ###########
#!/usr/bin/python

import random
u=0   #variable for number of users
count=0     #variable for number of users in the unit circle
for u in range(0,100):
	(X,Y)=(random.random()*2- 1, random.random()*2-1)
	u+=1
	
	if((X**2+Y**2)<=1):
		count+=1

perc=(float(count)/100)*100

print "Percentage of users in the unit circle around the MSC is %d" %perc
