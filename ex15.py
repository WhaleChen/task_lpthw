#-*- coding:utf-8 -*-
# "Hard coding" means putting some bit of information that should come from the user as a string directly in our source code.
from sys import argv
script, filename=argv
txt=open(filename)
# open file does not necessarily show the file,only making it alive.

print "Here's your file %r:" % filename
print txt.read()
# show the file using .read()

print "Type the filename again:"
file_again=raw_input(">")
# also we can get the filename through raw_input 
txt_again=open(file_again)

print txt_again.read()



