#using one line to copy...

#-*- coding:utf:9 -*-

from sys import argv
from os.path import exists

script, from_file, to_file=argv

open(to_file,'w').write(open(from_file).read())

