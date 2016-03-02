# -*- coding: utf-8 -*-
#编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def log(func):
	def wrapper(*args, **kw):
		print 'begin call %s()' % func.__name__
		func(*args, **kw)
		print 'end call %s()' % func.__name__
	return wrapper
	
@log
def now():
	print '2016-3-2'
	
now()