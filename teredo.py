'''
        def walk(dir, relations_of_tree, objs_of_tree):
            for name in os.listdir(dir.name):
                path = os.path.join(dir.name, name)
                path_obj = self.node(path, len(objs_of_tree))
                relations_of_tree += [[dir.id, path_obj.id]]
                objs_of_tree += [path_obj]
                if os.path.isdir(path):
                    walk(path_obj, relations_of_tree, objs_of_tree)
            self.tree = relations_of_tree
            self.objs = objs_of_tree

        walk(self.root, [], [self.root])
'''

"""
Классовая зависимость:  <class_os -> Tree -> Node -> Teredo

Словарь устанавливает соответствие между базовым множеством объектов и его классом-обработчиком

tree_parsers - словарь { forest:       --- строка --- базовое множество объектов (лес): "html", "site", "os"...
                        builder_class  --- класс --- атрибуты и методы базового множества
                        }



"""


import os

class class_os(object):

    def _root(self, descriptor="."):
        return Node(name = os.path._getfinalpathname(descriptor),
                    terminal = not os.path.isdir(descriptor),
                    basename = os.path.basename(descriptor))

    def _branches(self, parent):
        return [Node(name = os.path._getfinalpathname(name),
                     terminal = not os.path.isdir(name),
                     basename = os.path.basename(name))
                for name in os.listdir(parent.name)]

class Tree(class_os):

    def __init__(self):
        self.bin_tree = []
        self.objs = []

    def walk(self,parent):
        for node in self._branches(parent):
            if not node.terminal:
                walk(node)

    def find(self,selector):
        return [node_obj for node_obj in self.objs if node_obj.basename.startswith(selector) and node_obj.type == 'DIR']



"""
Функция принимает:
                    root : корневой объект дерева для разбора (строка)
                    forest: параметр разбора (строка): "html", "site", "os" etc
                возвращает:
                    дерево узловых объектов (словарь)
"""


class Node(Tree):
    def __init__(self, parent, **kwargs):
        self.id = len(Tree.objs)
        Tree.objs += self
        if parent: Tree.bin_tree += [(parent.id,self.id)]
        for attr, value in kwargs.items():
            setattr(self, attr, value)


class Teredo(Node):
    def __init__(self,descriptor):
        self.root = self._root(descriptor)


tree_parsers = {"os": class_os}
forest = "os"
builder_class = tree_parsers[forest]

pars = Teredo("C:\Projects\My-Projects")

print(pars.__dir__())

'''

for item in pars.find("p"):
    print(item.basename)

for item in pars.objs:
    print(item.id, ' =====> ', item.basename)

for item in pars.tree:
    print("(", pars.objs[item[0]].type, ")",  pars.objs[item[0]].basename,
          " =====> ",
          "(", pars.objs[item[1]].type, ")", pars.objs[item[1]].basename)


# print(pars.root)
# print(pars.tree)

'''