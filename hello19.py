# coding: UTF-8
# 関数
def hello():
	print "hello"

hello()

def hello(name):
	print "hello %s!" %name

hello("tom")
hello("steve")

def hello(name, num):
	print "hello %s! " %name * num

hello("tom", 2)
hello("steve", 3)

def hello(name, num = 4):
  print "hello %s! " %name * num

hello("tom")
hello("steve")
hello(num = 2, name = "fkoji")

def hello(name, num = 3):
	return "hello %s! " % name * num
s = hello("steve")
print s
