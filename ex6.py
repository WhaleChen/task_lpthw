#-*- codling: utf-8-*-
x = "There are %d types of people." %10 
# 10 types 
binary ="binary" # define binary
do_not ="don't" # define do_not 
y = "Those who know %s and those who %s." %(binary,do_not)
# s stand for string  one by one.
print x
print y
# print x and y
print "I said %r." %x
print "I also said:'%s'."%y
#print can also using the structure of %
hilarious =False
joke_evaluation = "Isn't that joke so funny?! %r"
# define also could be with %r,funny! See the tolerance of the defination.
print joke_evaluation %hilarious
# flexible print method
w= "This is the left side of ..."
e= "a string with a right side."
print w +e
#print could combine string directly by using '+'
