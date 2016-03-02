# -*- coding: utf-8 -*-
#raise error

def devision(s):
	n = int(s)
	return 10 / n
	
def bar(s):
	try: # try 处的block如果遇到错误则不继续执行，转去执行except
		return devision(s) * 2
	except StandardError, e:
		#print 'error'
		raise
		
def main():
	bar('0')
	
main()
