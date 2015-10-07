#-*- coding: utf-8-*-
#-*- coding: cp936-*-
# 对注释有要求
name = 'Whale Chen'
age = 30 #not a lie
height = 172 #cm
# 1 inche equal to 2.54 cm
weight =58 #kg
# 1 pound equal to 0.4536 kg 
eyes = 'black'
teeth ='White' # a lie
hair ='black'

print "let's talk about %s." %name
print "He's %d cm tall." %height
print "He's %d kg heavy." %weight
print "Atually that's not too slim."
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee." %teeth
print "If I add %d,%d and %d I get %d." %(age, height, weight, age +height+height) 

'''
%%百分号标记
%c字符及其ASCII码
%s字符串
%d有符号整数(十进制)
%u无符号整数(十进制)
%o无符号整数(八进制)
%x无符号整数(十六进制)
%X无符号整数(十六进制大写字符)
%e浮点数字(科学计数法)%E浮点数字(科学计数法，用E代替e)
%f浮点数字(用小数点符号)
%g浮点数字(根据值的大小采用%e或%f)
%G浮点数字(类似于%g)
%p指针(用十六进制打印值的内存地址)
%n存储输出字符的数量放进参数列表的下一个变量中...
'''
