# coding=utf-8

from teredo import *

a = [1,2,(3,4,[6,7,True]),dict(x=2,y=True)]

t = Teredo(a, 'py.obj')
print(t.get_pattern(wrapper_element=lambda x: '\t' * x.floor + (x.name if x.isnode and x.name != 'str' else str(x.content)) + '\n',
                                    wrapper_open=lambda x: '',
                                    wrapper_between=lambda x: '',
                                    wrapper_close=lambda x: '',
                                    filterer=lambda x: True))
