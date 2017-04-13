# coding=utf-8

from teredo import *

class Tree_Module(object):
    def __init__(self, root_script):
        self._root = root_script
    def _str(self):
        return self.name
    def _childs(self, parent=None):
        def get_path(name):
            return (parent.path + '.' if parent else '') + name
        if parent is None:
            list_of_childs = [self._root]
        else:
            # print(parent.name)
            try:
                list_of_childs = [child for child in eval('{}.__dict__'.format(parent.path)) if callable(eval(parent.path+'.'+child))]
            except:
                list_of_childs = []
        return [{'name': name,
                 'isnode': True,
                 'classo': eval(get_path(name) + '.__class__.__name__'),
                 'doc': eval(get_path(name) + '.__doc__'),
                 'path': get_path(name)}
                for name in list_of_childs]

import re
t = Teredo('re', Tree_Module)
print(t.get_pattern(wrapper_element=lambda x: ('\t' * x.floor + x.name + '(' + x.classo + '):' + '\n'),
                                    wrapper_open=lambda x: '',
                                    wrapper_between=lambda x: '',
                                    wrapper_close=lambda x: ''))


import re
t = Teredo('re', Tree_Module)
print(t.get_pattern(wrapper_element=lambda x: ('\t' * x.floor + x.name + '(' + x.classo + '):' + '\n') + ('\t'*(x.floor+1) + x.doc if x.doc else ''),
                                    wrapper_open=lambda x: '',
                                    wrapper_between=lambda x: '',
                                    wrapper_close=lambda x: ''))
