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
            return str(self.tag)

        def _childs(self, parent=None):
            list_of_childs = list(parent.tag) if parent else [self._root]
            return [{'name': element.name,
                     'isnode': element.name != None,
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
        # рекурсивно проходим по дереву и генерим все его элементы
        def walk(parent):
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
        self.elements = [self.root]
        walk(self.root)

    @staticmethod
    def get_root(obj):
        return obj.root if obj.__class__.__name__ == 'Teredo' else obj

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

    def ShowTree(self, format=None):
        root = Tree.get_root(self)
        str_tree = ''
        if not format:
            format = lambda x: '\t' * x.floor + x.name + '\n'
        for element in Tree.iterate_tree(root):
            if element.isnode:
                str_tree += format(element)
        return str_tree

    def ShowFunc(self):
        root = Tree.get_root(self)
        prev_element = root
        for element in Tree.iterate_tree(root):
            if element == root:
                str_tree = root.name
            elif prev_element.floor < element.floor :
                str_tree += '(' + element.name
            elif prev_element.floor == element.floor:
                str_tree += ',' + element.name
            else:
                str_tree += ')'*(prev_element.floor-element.floor) + ', ' + element.name
            prev_element = element
        return str_tree + ')'*prev_element.floor

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

    def Next(self,distance=1):
        if not self.parent: return None
        return self.parent.childs[self.parent.childs.index(self)+distance]

    def Previous(self,distance=1):
        if not self.parent: return None
        return self.parent.childs[self.parent.childs.index(self)+distance]

    def Down(self):
        return self.childs[0]

    def LikeIt(self, elem_pattern=lambda x: x.name, elem_filter=lambda x: x.isnode):
        print(super())
        return [element for element in Tree.iterate_tree(self.root) if elem_filter(element) and elem_pattern(element) == elem_pattern(self)]


class Teredo(Element):
    def __init__(self,descriptor,forest="html"):
        self.tree = Tree(descriptor)
        self.root = self.tree.root
        self.root.ancestor = self

    def __getattr__(self, item):
        print(getattr(self.root,item))