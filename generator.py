# -*- coding: utf-8 -*-
#生成器
#key word:yield
def fib(maxn):
	n, num1, num2 = 0, 0, 1
	while n < maxn:
		yield num2
		num1, num2 = num2, num1 + num2 
		n = n + 1
		
g = fib(8)
i = 0
while i <5:
	i =i + 1
	print g.next()
	
	
print g