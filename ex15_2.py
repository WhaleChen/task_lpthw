#-*- coding:utf-8 -*-
print "Pls input the filename you want to open."
file_again=raw_input(">")
# also we can get the filename through raw_input 
txt_again=open(file_again)

print txt_again.read()
