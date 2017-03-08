class A(object):
    def __init__(self,name):
        self.name = name
        self.old = len(name)
        self.title = 'AAAAAAAAAAA'

class B(A):
    def __init__(self,name):
        self.root = A(name)
    def __getattr__(self, item):
        print('I am')
        getattr(self.root,'title')

    pass

a = A('ME')
# print(a.name)
# print(getattr(a,'name'))

b=B('BBB')
print(b.name)
print(b.old)