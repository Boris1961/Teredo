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
Словарь устанавливает соответствие между базовым множеством объектов и его классом-обработчиком

tree_parsers - словарь { forest:       --- строка --- базовое множество объектов (лес): "html", "site", "os"...
                        builder_class  --- класс --- атрибуты и методы базового множества
                        }
"""

import os
tree_parsers = {"os": class_os}
forest = "os"
builder_class = tree_parsers[forest]


class class_os(object):

    def __init__(self, root="."):
        self.root = root
        self.tree = []
        self.objs = []

    class node(object):
        def __init__(self, path, id):
            self.name = path
            self.basename = os.path.basename(path)
            self.id = id
            self.type = "DIR" if os.path.isdir(path) else "FILE"

    def list_of_suns(self, parent):
        return [get_node(_name = name,
                         _terminal = not os.path.isdir(name),
                         basename = os.path.basename(name))
                for name in os.listdir(parent.name)]


        for name in os.listdir(dir.name):
            path = os.path.join(dir.name, name)
            path_obj = self.node(path, len(self.tree))
            self.tree += [[dir.id, path_obj.id]]
            self.objs += [path_obj]
            if os.path.isdir(path):
                walk(path_obj)

    def find(self,selector):
        return [node_obj for node_obj in self.objs if node_obj.basename.startswith(selector) and node_obj.type == 'DIR']

class builder_class(object):

    def __init__(self):
        self.tree = []
        self.objs = []

    def walk(self,node):
        for

        for name in os.listdir(dir.name):
            path = os.path.join(dir.name, name)
            path_obj = self.node(path, len(self.tree))
            self.tree += [[dir.id, path_obj.id]]
            self.objs += [path_obj]
            if os.path.isdir(path):
                walk(path_obj)


"""
Функция принимает:
                    root : корневой объект дерева для разбора (строка)
                    forest: параметр разбора (строка): "html", "site", "os" etc
                возвращает:
                    дерево узловых объектов (словарь)
"""


class Teredo():
    pass


pars = builder_class("C:\Projects\My-Projects")

for item in pars.find("p"):
    print(item.basename)


'''
for item in pars.objs:
    print(item.id, ' =====> ', item.basename)

for item in pars.tree:
    print("(", pars.objs[item[0]].type, ")",  pars.objs[item[0]].basename,
          " =====> ",
          "(", pars.objs[item[1]].type, ")", pars.objs[item[1]].basename)


# print(pars.root)
# print(pars.tree)

'''