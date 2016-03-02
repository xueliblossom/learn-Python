# -*- coding: utf-8 -*-
#编写一个不管是否传递参数都能运行的装饰器
def log(label):
	if callable(label): # callable接收的若是可调用对象则返回True，否则返回False
		def wrapper(*args, **kw):
			print'call %s()' % label.__name__
			label(*args, **kw)
		return wrapper
	else:
		def decorator(func):
			def wrapper(*args, **kw):
				print '%s call %s()' % (label, func.__name__)
				func(*args, **kw)
			return wrapper
		return decorator
#即now = log(now)		
@log
def now():
	print '2016-3-2'
		
now()


#即now = log('heyan')(now)
@log('heyan')
def now():
	print '2016-3-2'
	
now()