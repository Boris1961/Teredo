'''
Классовая зависимость:  Real_tree -> Tree -> TeredoElement -> Teredo
'''

class Tree_EXPRESSION(object):
    pass

class Tree_WEB(object):
    pass


import os
class Tree_OS(object):
    def __init__(self, root_script):
        self._root = os.path.abspath(root_script)

    def _str(self):
        return self.path

    def _childs(self, parent=None):
        try:
            # childs = os.listdir(parent.path) if parent else []
            list_of_childs = [os.path.join(parent.path, element) for element in
                              os.listdir(parent.path)] if parent else [self._root]
        except:
            list_of_childs = []
        return [{'name': os.path.basename(name),
                 'isnode': os.path.isdir(name),
                 'path': os.path.abspath(name)}
                for name in list_of_childs]

class Tree_HTML(object):

    def __init__(self, root_script):
        from bs4 import BeautifulSoup
        import requests

        try:
            root_script = requests.get(root_script).content
        except:
            raise RuntimeError("Something bad happened")

        self._root = BeautifulSoup(root_script, 'html.parser')

    def _str(self):
        return self.tag

    def _childs(self, parent=None):
        list_of_childs = list(parent.tag) if parent else [self._root]
        return [{'name': element.name if element.name else '<Text>',
                 'isnode': element.name != None ,
                 'tag': element}
                for element in list_of_childs]

'''
Класс TeredoTree: абстрактное дерево:
    Атрибуты:   root : type=TeredoElement: корневой элемент дерева
                elements: type=list: список всех элементов (объектов класса TeredoElement) дерева
                handler: type=type: класс-контейнер user-дерева (например, встроенные Tree_HTML или Tree_OS)


'''
class TeredoTree(object):
    def __init__(self, root_script, class_handler):
        def walk(parent):
            # рекурсивно проходим по дереву и генерим все его элементы
            for child_dict in class_handler._childs(self,parent):
                child = TeredoElement(parent, child_dict)
                child.id = len(self.elements)
                child.root = self.root
                self.elements.append(child)
                parent.childs.append(child)
                if child.isnode:
                    walk(child)
        class_handler.__init__(self,root_script)
        root = TeredoElement(None, class_handler._childs(self)[0]) # генерим корневой элемент дерева
        self.handler = class_handler
        self.root = root.root = root
        self.elements = [root]
        root.id = 0
        root.tree = self
        walk(root)

    def __str__(self):
        return object.__str__(self.root.tree.handler._str(self))

    __repr__ = __str__

    # итератор дерева
    @staticmethod
    def iterate_tree(root, touch=False):
        if not touch:
            yield root
        for element in root.childs:
            yield element
            if element.isnode:
                for child in TeredoTree.iterate_tree(element, True):
                    yield child

    def get_pattern(self, dist=list(), wrapper_body=lambda x:x.name, wrapper_open=lambda x:'(',  wrapper_between=lambda x:',', wrapper_close=lambda x:')', filterer=lambda x:x.isnode):
        def iterate_tree(element, dist):
            list_childs = list(filter(filterer,element.childs))
            str_tree = wrapper_body(element) + wrapper_open(element)
            for child in list_childs:
                str_tree += iterate_tree(child,dist)
                if list_childs[-1] != child:
                    str_tree += wrapper_between(child)
            str_tree += wrapper_close(element)
            if dist.__class__.__name__ == 'dict' :
                dist[element] = str_tree
            return str_tree
        str_tree = iterate_tree(self, dist)
        if dist.__class__.__name__ == 'list':
            return str_tree
        else:
            return dist

    def get_postfix(self, wrapper_body=lambda x:x.name):
        post_list = []
        for element in TeredoTree.iterate_tree(self):
            post_list = (['func(%i)<%s>' % (len(element.childs), wrapper_body(element))] if element.isnode else ['arg<%s>' % wrapper_body(element)]) + post_list
        return post_list


    def ShowPostfix(self):
        pass

    def Select(self, selector):
        pass

class TeredoElement(TeredoTree):
    def __init__(self, parent, kwargs):
        if parent:
            self.floor = parent.floor + 1
            self.parent = parent
        else:
            self.floor = 0
            self.id = 0
            self.parent = None
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        self.childs = []

    def __getattr__(self, item):
        if not self.isnode:
            return None

        nodes = [child for child in self.parent.childs if child.isnode] if self.parent else [self]

        if item.lower() == 'next':
            try:
                return nodes[nodes.index(self):][1]
            except:
                return None

        if item.lower() == 'previous':
            try:
                return nodes[:nodes.index(self)][-1]
            except:
                return None

        if item.lower() == 'down':
            try:
                return [child for child in self.childs if child.isnode][0]
            except:
                return None

        if item.lower() == 'up':
            try:
                return self.parent
            except:
                return None

        if item.lower() == 'showfunc':
            return self.get_pattern()

        if item.lower() == 'showtree':
            return self.get_pattern(wrapper_body=lambda x: '\t' * x.floor + x.name + '\n',
                                    wrapper_open=lambda x: '',
                                    wrapper_between=lambda x: '',
                                    wrapper_close=lambda x: '')

        if item.lower() == 'showpostfix':
            return self.get_postfix(wrapper_body=lambda x:x.name)

        if item.lower() == 'showpath':
            element = self
            path = []
            while element.parent:
                path = [element.name] + path
                element = element.parent
            return path

        return getattr(self.root, item)

    def LikeIt(self, elem_pattern=lambda x: x.name, elem_filter=lambda x: x.isnode):
        return [element for element in TeredoTree.iterate_tree(self.root) if elem_filter(element) and elem_pattern(element) == elem_pattern(self)]


'''
    Teredo-дерево.
    Атрибут экземпляра: .root = корневой элемент дерева (класс TeredoElement)
'''
class Teredo(TeredoElement):
    def __init__(self,descriptor,forest="html"):
        if forest.lower() == 'html':
            self.tree = TeredoTree(descriptor, Tree_HTML)
        if forest.lower() == 'os':
            self.tree = TeredoTree(descriptor, Tree_OS)
        if forest.__class__.__name__ == 'type':
            self.tree = TeredoTree(descriptor, forest)

        self.root = self.tree.root
        self.root.ancestor = self

    def __getattr__(self, item):
        return getattr(self.root, item)
