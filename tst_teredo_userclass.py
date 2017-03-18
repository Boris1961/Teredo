# coding=utf-8
from teredo import *


class General(type):
    pass

class A(metaclass= General):
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

class A1():
    pass

class B1(A1):
    pass

class C1(B1):
    pass

class D1(C1):
    pass

def F():
    a = 1
    print('F: ', locals())
    # print(globals())

f = F()
# print(B3.mro())

a0 = A()
a1 = A()

b0 = B()
b1 = B()
b2 = B()



class Tree_Typos(object):
    global_list = list(globals().keys())
    def __init__(self, root_script):
        self._root = root_script
    def _str(self):
        return self.name
    def _childs(self, parent=None):
        if parent == None:
            list_of_childs = [self._root]
        else:
            list_of_childs = [name for name in Tree_Typos.global_list if
                              eval('type(%s).__name__=="%s"' % (name, parent.name))]
        return [{'name': name,
                 'isnode': True}
                for name in list_of_childs]

