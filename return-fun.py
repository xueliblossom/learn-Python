# -*- coding: utf-8 -*-
#闭包函数和匿名函数

def count():
	fun = []
	for i in range(1, 4):
		def f():
			return i * i
		fun.append(f)
	return fun
	
fun1, fun2, fun3 = count()
print fun1(), fun2(), fun3() #因为返回函数只在调用的时候才执行，所以当三个函数都返回时
                             #i=3,因此结果都为9，所以避免在返回函数使用循环变量，如count2
def count1():
	Fun = []
	for j in range(1, 4):
		def f(k):
			def g():
				return k * k
			return g
			
		Fun.append(f(j))
		
	return Fun
	
Fun1, Fun2, Fun3 = count1()
print Fun1(), Fun2(), Fun3()
			
		