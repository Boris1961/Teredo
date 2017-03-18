# coding=utf-8

from teredo import *

demo_menu = """
     Демо Teredo может:
         0: выходить из себя
         1: делать Teredo-дерево из любого древесного объекта:
                Teredo(root_desc, tree_desc)
                 root_desc = дескриптор корня дерева (строка )
                 tree_desc = дескриптор древесной структуры встроеннного дерева (строка)
                             или класс-обработчик древесной структуры для пользоват. дерева
                  Пример: tree_teredo = Teredo('facebook.com', 'html')
                          tree_teredo = Teredo('С:\', 'os')

         2: уходить в корeнь: tree_element = tree_teredo.root
         3: двинуть вниз по дереву: tree_element = tree_element.down
         4: двинуть вверх по дереву: tree_element = tree_element.parent
         5: вправо по дереву: tree_element = tree_element.next
         6: влево по дереву: tree_element = tree_element.previous
         7: нарисовать поддерево от заданного гнезда (древесный вид): tree_element.showtree
         8: .... (префиксный вид): tree_element.showfunc
         9: .... (постфиксный вид): tree_element.showpostfix
        10: нарисовать путь к гнезду от корня: tree_element.showpath
        11: показать список дочерних гнёзд tree_element.childs
        12: пример пользовательского дерева (Tree_Typos)

        Что делать:
"""

act = -1
element_teredo = None
while act != 0:

    if act == -1:
        try:
            act = int(input(demo_menu))
        except ValueError:
            continue
    else:
        try:
            act = input('...')
            if act == '':
                try:
                    act = int(input(demo_menu))
                except ValueError:
                    continue
            else:
                try:
                    act = int(act)
                except ValueError:
                    continue
        except ValueError:
            continue

    if act == 1 or element_teredo is None:
        while True:
            item = int(input("Дерево:\n 1. HTML\n 2.OS\n"))-1
            if item == 0 or item == 1:
                desc = ['html','os'][item]
                tree_root = input(["HTML или URL:\n", "Имя папки:"][item])
                try:
                    element_teredo = Teredo(tree_root, desc)
                except:
                    continue
                element_to_demo = element_teredo
                str_teredo = 'Teredo("%s", "%s")' % (tree_root, desc)
                str_to_demo = str_teredo
                break

    elif act == 2:
        element_to_demo = element_teredo.root
        str_to_demo = 'Teredo(%s, %s).root' % (tree_root, desc)

    elif act == 3:
        element_to_demo = element_teredo.down
        str_to_demo = str_teredo + '.down'

    elif act == 4:
        element_to_demo = element_teredo.parent
        str_to_demo = str_teredo + '.parent'

    elif act == 5:
        element_to_demo = element_teredo.next
        str_to_demo = str_teredo + '.next'

    elif act == 6:
        element_to_demo = element_teredo.previous
        str_to_demo = str_teredo + '.previous'

    elif act == 7:
        element_to_demo = element_teredo.showtree
        str_to_demo = str_teredo + '.showtree'

    elif act == 8:
        element_to_demo = element_teredo.showfunc
        str_to_demo = str_teredo + '.showfunc'

    elif act == 9:
        element_to_demo = element_teredo.showpostfix
        str_to_demo = str_teredo + '.showpostfix'

    elif act == 10:
        element_to_demo = element_teredo.showpath
        str_to_demo = str_teredo + '.showpath'

    elif act == 11:
        element_to_demo = element_teredo.childs
        str_to_demo = str_teredo + '.childs'

    elif act == 12:
        from tst_teredo_userclass import *
        element_teredo = Teredo('type', Tree_Typos)
        str_teredo = "Teredo('type', Tree_Typos)"
        element_to_demo = element_teredo.showtree
        str_to_demo = str_teredo

    print('\n%s = \n%s' % (str_to_demo, element_to_demo))
    if element_to_demo.__class__.__name__ == 'TeredoElement':
        element_teredo = element_to_demo
        str_teredo = str_to_demo
