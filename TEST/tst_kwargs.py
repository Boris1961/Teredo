class ill(object):
    id = 0
    def __init__(self, **kwargs):
        self.id = ill.id
        ill.id += 1
        for attr,value in kwargs.items():
            setattr(self, attr, value)

# print(ill(name='me',temp='hot').id)
# print(ill(name='you',temp='cold').id)

def get_kwargs():
    return {'a1':1, 'a2':2, 'a3':3}

class cl_kwargs(object):
    def __init__(self,dict):
        for attr,value in dict.items():
            setattr(self, attr, value)

cl = cl_kwargs(get_kwargs())

print(cl.__dict__)
