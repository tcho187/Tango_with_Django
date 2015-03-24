#!/usr/local/bin/python
import csv

results=[]

with open ('triangle.txt') as inputfile:
	results =list (csv.reader(inputfile))

