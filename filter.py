# -*- coding: utf-8 -*-
#使用filter删除1-100之间的素数
def isPrime(x):
    if x < 4:
        return 0
    else:
        for i in range (2, x):
            if x % i == 0: #条件不满足返回的是none吗
                return x #这里的返回，是条件满足就返回然后退出循环吗

print filter(isPrime, range(1, 101))