import csv

results=[]

with open ('triangle.txt') as inputfile:
	results =list (csv.reader(inputfile))

# print results


print results[2]