#-*- coding:utf-8 -*-


def printNumberLists(m):
	i=0
	numbers=[]

	while i<m:
		print "At the top i is %d" %i
		numbers.append(i)

		i+=1
		print "Numbers now:", numbers
		print "At the bottom i is %d"%i

	print "The numbers: "

	for num in numbers:
		print num 

	return numbers

m=int(raw_input("Please enter a number: "))
printNumberLists(m)
