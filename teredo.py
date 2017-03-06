'''
Классовая зависимость:  Real_tree -> Tree -> Element -> Teredo

Словарь устанавливает соответствие между базовым множеством объектов и его классом-обработчиком

tree_parsers - словарь { forest:       --- строка --- базовое множество объектов (лес): "html", "site", "os"...
                        builder_class  --- класс --- атрибуты и методы базового множества
                        }
'''

import os
class Real_Tree(object):
    def __init__(self,root_script):
        self._root = root_script
    def _childs(self, parent=None):
        try:
            # childs = os.listdir(parent.path) if parent else []
            list_of_childs = [os.path.join(parent.path, element) for element in os.listdir(parent.path)] if parent else [self._root]
        except:
            list_of_childs = []
        return [{'name' : os.path.basename(name),
                 'isnode' : os.path.isdir(name),
                 'path': os.path.abspath(name)}
                for name in list_of_childs]

class Tree(Real_Tree):
    STR_TREE = ''

    def __init__(self, root_script):
        def walk(parent):
            for child in self._childs(parent):
                child_obj = Element(self.bin_tree, self.objs, parent, child)
                parent.childs += [child_obj]
                if child_obj.isnode:
                    walk(child_obj)
        # self.str_tree = Real_Tree(root_script)
        self.bin_tree = []
        self.objs = []
        self.root = Element(self.bin_tree,self.objs,None,Real_Tree(root_script)._childs()[0])
        walk(self.root)

    def ShowTree(self, file=None):
        root = self.root if self.__class__.__name__ == 'Teredo' else self
        Tree.STR_TREE = root.name + '\n'
        def walk(parent):
            for child in parent.childs:
                Tree.STR_TREE += '  '*child.floor + child.name + '\n'
                if child.isnode:
                    walk(child)
            if parent.floor==0: return Tree.STR_TREE
        return (walk(root))


class Element(Tree):
    def __init__(self, bin_tree, objs, parent, kwargs):
        self.id = len(objs)
        objs += [self]
        if parent:
            bin_tree += [(parent.id, self.id)]
            self.floor = parent.floor + 1
            self.parent = parent
        else:
            self.floor = 0
            self.parent = None
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        # if self.isnode: self.childs = []
        self.childs = []

    def neighbor(self,distance=1):
        if not self.parent: return None
        indx = self.parent.childs[self]
        return self.parent.childs[indx+distance]

    def LikeIt(self, *elem_criteria, **elem_filter):
        if not elem_filter:
            elem_filter = {'isnode':True}
        if not elem_criteria:
            elem_criteria = ['floor']
        print(t.objs)


class Teredo(Element):
    def __init__(self,descriptor):
        self.tree = Tree(descriptor)
        self.root = self.tree.root
        self.root.instante = self


    # tree_parsers = {"os": Real_Tree}
# forest = "os"
# builder_class = tree_parsers[forest]

'''

pars = Teredo("d:\E Мои документы")

# C:\Projects\My-Projects

# print(pars.__dir__())

for item in sorted(pars.tree.objs, key=lambda x: x.isnode):
    print(item.isnode, ' =====> ', item.name)

for item in pars.tree.bin_tree :
    if pars.tree.objs[item[1]].isnode :
        print("(", pars.tree.objs[item[0]].isnode, ")",  pars.tree.objs[item[0]].name,
              " =====> ",
              "(", pars.tree.objs[item[1]].isnode, ")", pars.tree.objs[item[1]].name)

# print(pars.root)
# print(pars.tree)
'''
