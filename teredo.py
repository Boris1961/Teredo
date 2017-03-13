'''
Классовая зависимость:  Real_tree -> Tree -> Element -> Teredo
'''

class Real_Tree_EXPRESSION(object):
    pass

class Real_Tree_WEB(object):
    pass


import os
class Real_Tree_OS(object):
    def __init__(self, root_script):
        self._root = root_script

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

class Real_Tree_HTML(object):

    def __init__(self, root_script):
        from bs4 import BeautifulSoup
        self._root = BeautifulSoup(root_script, 'html.parser')

    def _str(self):
        return self.tag

    def _childs(self, parent=None):
        list_of_childs = list(parent.tag) if parent else [self._root]
        return [{'name': element.name if element.name != None else '<Text>',
                 'isnode': element.name != None ,
                 'tag': element}
                for element in list_of_childs]

'''
Класс-ДЕРЕВО Tree:
    Атрибуты:   root : type=Element: корневой элемент дерева
                elements: type=list: список всех элементов дерева
                handler: type=type: класс-контейнер user-дерева


'''

class Tree(object):
    def __init__(self, root_script, class_handler):
        def walk(parent):
            # рекурсивно проходим по дереву и генерим все его элементы
            for child_dict in class_handler._childs(self,parent):
                child = Element(parent, child_dict)
                child.id = len(self.elements)
                child.root = self.root
                self.elements.append(child)
                parent.childs.append(child)
                if child.isnode:
                    walk(child)
        class_handler.__init__(self,root_script)
        root = Element(None, class_handler._childs(self)[0]) # генерим корневой элемент дерева
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
                for child in Tree.iterate_tree(element, True):
                    yield child

    # @staticmethod

    def get_pattern(self, wrapper_body=lambda x:x.name, wrapper_open=lambda x:'(',  wrapper_between=lambda x:',', wrapper_close=lambda x:')', filterer=lambda x:x.isnode):
        prev_element = self
        for element in Tree.iterate_tree(self):
            if not filterer(element):
                continue
            elif element == self:
                str_tree = wrapper_body(self)
            elif prev_element.floor < element.floor :       # вниз по дереву
                str_tree += wrapper_open(element) + wrapper_body(element)
            elif prev_element.floor == element.floor:       # вправо по дереву
                str_tree += wrapper_between(element) + wrapper_body(element)
            else:                                           # вверх по дереву
                str_tree += wrapper_close(element)*(prev_element.floor-element.floor) + wrapper_between(element) + wrapper_body(element)
            prev_element = element
        return str_tree + wrapper_close(element)*prev_element.floor

    def get_pattern_all(self, wrapper_body=lambda x:x.name, wrapper_open=lambda x:'(',  wrapper_between=lambda x:',', wrapper_close=lambda x:')', filterer=lambda x:x.isnode):

        def proc_tuple(element, dict_patt):
            list_childs = list(filter(filterer,element.childs))
            list_tree = [wrapper_body(element), wrapper_open(element)]
            for child in list_childs:
                list_tree += proc_tuple(child,dict_patt)
                if list_childs[-1] != child:
                    list_tree.append(wrapper_between(child))
            list_tree.append(wrapper_close(element))
            dict_patt[element] = ''.join(list_tree)
            return list_tree

        dict_patt = dict()
        proc_tuple(self, dict_patt)
        return dict_patt

    def ShowPostfix(self):
        pass

    def Select(self, selector):
        pass

class Element(Tree):
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

        return getattr(self.root, item)

    def LikeIt(self, elem_pattern=lambda x: x.name, elem_filter=lambda x: x.isnode):
        return [element for element in Tree.iterate_tree(self.root) if elem_filter(element) and elem_pattern(element) == elem_pattern(self)]


'''
        Словарь устанавливает соответствие между базовым множеством объектов и его классом-обработчиком
        tree_parsers - словарь { forest:       --- строка --- базовое множество объектов (лес): "html", "site", "os"...
                            builder_class  --- класс --- атрибуты и методы базового множества
'''
class Teredo(Element):
    def __init__(self,descriptor,forest="html"):
        if forest.lower() == 'html':
            self.tree = Tree(descriptor, Real_Tree_HTML)
        if forest.lower() == 'os':
            self.tree = Tree(descriptor, Real_Tree_OS)
        if forest.__class__.__name__ == 'type':
            self.tree = Tree(descriptor, forest)

        self.root = self.tree.root
        self.root.ancestor = self

    def __getattr__(self, item):
        return getattr(self.root, item)
