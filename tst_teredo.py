from teredo import Teredo
t = Teredo('C:\\Projects\\Learn3')

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

print(t.root.instante.__name__)

# print(t.ShowTree())

# print(t.ShowTree())
# print(t.root.ShowTree())
