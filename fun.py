# -*- coding: utf-8 -*-
# category of paremeter
def fun(x, y, z=1, *para1, **para2): # z 为默认参数 * 为可变参数， ** 为关键字参数
	print 'x =', x, 'y =', y, 'z =', z, 'para1 =', para1, 'para2 =', para2
	
fun(1,2)
fun(1, 2, (1, 2))
fun(1, 2, 7, 'heyan', 'luohui', uni1 = 'tinghua', uni2 = 'peking')