# -*- coding: utf-8 -*-
#列表生成式
string = ['Hello', 'HEYAN', 24, 'graduate']
l = [s.lower() if isinstance(s, str)  else s for s in string]
print l