'''
Классовая зависимость:  Real_tree -> Tree -> Element -> Teredo
Словарь устанавливает соответствие между базовым множеством объектов и его классом-обработчиком
tree_parsers - словарь { forest:       --- строка --- базовое множество объектов (лес): "html", "site", "os"...
                        builder_class  --- класс --- атрибуты и методы базового множества
                        }
'''

TYPE_OF_FOREST_OF_TREES_FOR_PARSING_THEM_BY_ME_FOR_ENJOY = "html"

if TYPE_OF_FOREST_OF_TREES_FOR_PARSING_THEM_BY_ME_FOR_ENJOY == "os":
    import os
    class Real_Tree(object):
        def __init__(self, root_script):
            self._root = root_script

        def __str__(self):
            return object.__str__(self.path)

        __repr__ = __str__

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


if TYPE_OF_FOREST_OF_TREES_FOR_PARSING_THEM_BY_ME_FOR_ENJOY == "html":
    from bs4 import BeautifulSoup
    class Real_Tree(object):
        def __init__(self, root_script):
            self._root = BeautifulSoup(root_script, 'html.parser')

        def __str__(self):
            return object.__str__(self.tag)

        __repr__ = __str__

        def _childs(self, parent=None):
            list_of_childs = list(parent.tag) if parent else [self._root]
            return [{'name': element.name if element.name != None else '<Text>',
                     'isnode': element.name != None ,
                     'tag': element}
                    for element in list_of_childs]


if TYPE_OF_FOREST_OF_TREES_FOR_PARSING_THEM_BY_ME_FOR_ENJOY == "expression":
    class Expression_Tree(object):
        pass


if TYPE_OF_FOREST_OF_TREES_FOR_PARSING_THEM_BY_ME_FOR_ENJOY == "site":
    class Site_Tree(object):
        pass

class Tree(Real_Tree):
    def __init__(self, root_script):
        def walk(parent):
            # рекурсивно проходим по дереву и генерим все его элементы
            for child_dict in self._childs(parent):
                child = Element(parent, child_dict)
                child.id = len(self.elements)
                child.root = self.root
                self.elements.append(child)
                parent.childs.append(child)
                if child.isnode:
                    walk(child)

        self.root = Element(None, Real_Tree(root_script)._childs()[0]) # генерим корневой элемент дерева
        self.root.id = 0
        self.root.root = self.root
        self.elements = [self.root]
        walk(self.root)

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
        root = self if self.parent else self.root
        prev_element = self.root
        for element in Tree.iterate_tree(root):
            if not filterer(element):
                continue
            elif element == root:
                str_tree = wrapper_body(root)
            elif prev_element.floor < element.floor :
                str_tree += wrapper_open(element) + wrapper_body(element)
            elif prev_element.floor == element.floor:
                str_tree += wrapper_between(element) + wrapper_body(element)
            else:
                str_tree += wrapper_close(element)*(prev_element.floor-element.floor) + wrapper_between(element) + wrapper_body(element)
            prev_element = element
        return str_tree + wrapper_close(element)*prev_element.floor

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


class Teredo(Element):
    def __init__(self,descriptor,forest="html"):
        self.tree = Tree(descriptor)
        self.root = self.tree.root
        self.root.ancestor = self

    def __getattr__(self, item):
        return getattr(self.root, item)
