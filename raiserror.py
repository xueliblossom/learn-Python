# -*- coding: utf-8 -*-
#raise error

def devision(s):
	n = int(s)
	return 10 / n
	
def bar(s):
	try:
		return devision(s) * 2
	except StandardError, e:
		#print 'error'
		raise
		
def main():
	bar('0')
	
main()
