#-*- coding:utf-8 -*-

# If the filename does not exist. The command will create automaticly.

from sys import argv

scrip, filename=argv

print "We're going to erase %r," %filename
print "If you don't want that ,hit CTRL-C(^C)."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
target=open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()
# truncate is essential with 'w' mode.

print "Noew I'm going to ask you for three lines."

line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(line1 +"\n"+line2+"\n"+line3 +"\n")

print "and finally, we close it."
target.close()

