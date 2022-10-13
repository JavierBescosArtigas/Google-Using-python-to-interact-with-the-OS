#!/usr/bin/env python3

#importaciones
import re
import csv
import operator
import sys

user = {}
errors = {}

#archivo del que leemos
logfile= './syslog.log'    #logfile = '/home/student-00-abf4ed01e396/syslog.log'
f = open(logfile, 'r')
#archivos donde escribimos
usersfile = './usersTohtml.csv' #usersfile = '/home/student-00-abf4ed01e396/users.csv'
errorsfile = './errorsTohtml.csv' #errorsfile = '/home/student-00-abf4ed01e396/errors.csv'

regex = r".*ticky: ([A-Z]+) ([\w ]+).*\(([\w.]+)\)$"

for log in f:
	result = re.search(r".*ticky: ([A-Z]+) ([\w ]+).*\(([\w.]+)\)$", log)
	if result.group(2) not in errors.keys():
		errors[result.group(2)] = 0
	errors[result.group(2)] += 1

	if result.group(3) not in user.keys():
		user[result.group(3)] = {} #empty dict-> key:dict
		user[result.group(3)]["INFO"] = 0
		user[result.group(3)]["ERROR"] = 0

	if result.group(1) == "INFO":
		user[result.group(3)]["INFO"] += 1
	elif result.group(1) =="ERROR":
		user[result.group(3)]["ERROR"] += 1
#sorting dicts.
errors = sorted(errors.items(), key = operator.itemgetter(1), reverse = True)
user = sorted(user.items())
#here it finishes reading logs and counting errors & users
f.close()
#print(errors)
#print(user)

#Lets continue with writing the files
f = open(errorsfile, "w")
for error in errors:
	errortext, errorcount = error
	f.write(str(errortext)+','+str(errorcount)+'\n')
f.close()

f = open(usersfile, "w")
f.write("Username,INFO,ERROR\n") #head of csv
for stats in user:
	user_info1, user_info2 = stats
	f.write(str(user_info1)+','+str(user_info2["INFO"])+','+str(user_info2["ERROR"])+'\n')
