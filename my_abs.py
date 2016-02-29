#learning function and how it raaise error
def my_abs(x): # define function name and parameter which are in()
	if not isinstance(x, (int, float)): # numbens whose type are int and float
		raise TypeError('bad operand type') # are enabled
	if x >= 0:
		return x
	else:
		return -x # the result can be get by function---return
		
