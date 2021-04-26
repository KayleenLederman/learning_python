#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math
data = []

for i in sys.argv[1: ]:      #add numbers inputted from terminal to data list
	data.append(float(i))
#print(data)

#Count
count = len(sys.argv[1: ])
print('Count:', count)

#Min
data.sort()
print('Minimum:', data[0])

#Max
print('Maximum:', data[-1])

#Mean
sum1 = 0
for n in data: sum1 += n
mean = sum1/len(sys.argv[1: ])
print('Mean:', mean)

#Std. Dev
sum2 = 0
for i in data:
	numerator = (i - mean) ** 2
	sum2 += numerator
std_dev = math.sqrt(sum2/count)
print('Std. dev:', std_dev)

#Median
if count % 2 ==  0: median = (data[int((count/2) - 1)] + data[int(count/2)])/ 2
else: median = data[int(len(data)/2)]	
#median = data[int(count/2)]			
print('Median:', median)
	

"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
