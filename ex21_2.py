#-*- coding:utf-8 -*-
def add(a,b):
	print "ADDING %d+%d" %(a,b)
	return a+b
def subtract(a,b):
	print "SUBRACTING %d-%d"%(a,b)
	return a-b
def multiply(a,b):
	print "MULITIPLY %d*%d"%(a,b)
	return a*b
def divide(a,b):
	print "DIVIDE %d/%d"%(a,b)
	return a/b

print "Let's do some math with just function!"

age =add(22,7)
height = subtract(174,2)
weight=multiply(58,2)
iq=divide(240,2)

print "Age: %d, Height: %d, Weight: %d, iq: %d"%(age, height, weight, iq)

