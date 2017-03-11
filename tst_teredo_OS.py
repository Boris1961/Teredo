# coding=utf-8

from teredo import *

t = Teredo('d:\DISC_I\EDIT','os')


#print('ShowTree: \n\n', t.showtree)
#print('ShowFunc: \n\n', t.showfunc)

print(t)
print(t.down)


'''
if False:
    for item in sorted(t.tree.objs, key=lambda x: x.isnode, reverse=True):
        try:
            print('node =', item.isnode,
                  'id, name: ', item.id, item.name,
                  'floor:', item.floor)
        except:
            print("ERROR: ", item.isnode, item.name, item.childs)

if False:
    for ch in t.root.childs:
        if ch.isnode:
            print( 'Node: ', ch.name, '(', len(ch.childs), ')' )
        else:
            print( 'Term: ', ch.name )

    print(t.root.childs[1].ShowTree())

    for ch in t.root.childs:
        if ch.isnode:
            print('DIR = ', ch.name, '\n    Childs:', [c.name for c in ch.childs])

if False:
    print(t.root.LikeIt())

# print(t.root.ancestor.root.path)
# print(t.root.LikeIt())
# print('SHOW: \n\n', t.root.childs[3].ShowTree())
# print( "\n".join(["(%d) : %s : %s" % (child.id, child.isnode, child.name) for child in t.root.childs]))

# print('SHOW-FUNC: \n\n', t.root.ShowFunc())
'''