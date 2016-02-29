# -*- coding: utf-8 -*-
#1.使用map函数和reduce函数
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
#2.Python提供的sum()函数可以接受一个list并求和，
#请编写一个prod()函数，可以接受一个list并利用reduce()求积。

def convert(name):
	 return name[0].upper() + name[1:].lower()
	
#map()函数接收两个参数，一个是函数，一个是序列，
#map将传入的函数依次作用到序列的每个元素
print map(convert, ['adam', 'LISA', 'barT'])

#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素做累积计算
def prod(list):
	def add(a, b):
		return a + b
	return reduce(add, list)
	
print prod([1, 2, 3])
	
	