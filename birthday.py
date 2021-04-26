#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

people = 25
days = 365
trial = 10000
duplicate = 0

for i in range(trial):
	#create empty calendar of zeros
	calendar = [] #new calendar each time
	for j in range(days):
		calendar.append(0)
	#print(calendar)
	
	#fill with random birthdays
	for j in range(people):
		birthday = random.randint(0, days-1)
		calendar[birthday] += 1
	#print(calendar)
	
	#check for duplication
	for day in calendar:
		if day > 1: duplicate += 1
		break # if calendar has collision, then stop
print(duplicate, trial, duplicate/trial)
		
"""
repeat for number of trials
	create empty calendar
	fill with random birthdays
	check for duplicates
	record
	wipe calendar
report duplicates/trial


"""


"""
python3 birthday.py
0.571
"""

