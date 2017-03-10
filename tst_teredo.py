# coding=utf-8

from teredo import *

if TYPE_OF_FOREST_OF_TREES_FOR_PARSING_THEM_BY_ME_FOR_ENJOY == "html":

    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    """

    import requests
    url = "https://laminat33.ru/category/laminat/balterio/?page=5"
    # url = "http://www.mvideo.ru/smartfony-i-svyaz/smartfony-205/f/category=iphone-914"

    # html_doc = requests.get(url).content

    t = Teredo(html_doc)

    print(t.root.get_pattern())
    # print('SHOW: \n\n', t.ShowTree(lambda x: "\t"*x.floor + "%s(%s)\n" % (x.name, len(x.tag.attrs))))
    # print('ShowTree: \n\n', t.showtree)
    # print('ShowFunc: \n\n', t.showfunc)


    # print('SHOW: \n\n', t.ShowTree(lambda x: "\t" * x.floor + "%s(%s)\n" % (x.name, len(x.tag.attrs))))
    # print('ShowFunc: \n\n', t.down)
    # print('SHOW: \n\n', t.down.down.ShowTree(lambda x: "\t" * x.floor + "%s(%s)\n" % (x.name, len(x.tag.attrs))))
    # print('=====',t.tree.elements[13].childs[1])
    # print('=====',t.tree.elements[13].childs[1].LikeIt()[0])
    # print('=====',t.tree.elements[13].childs[1].LikeIt()[1])
    # print(t.tree.elements[10].LikeIt()[0].tag)
    # print('SHOW: \n\n', t.ShowTree(lambda x: "\t" * x.floor + "%s(%s)\n" % (x.name, ','.join(list(x.tag.attrs.keys())))))


if TYPE_OF_FOREST_OF_TREES_FOR_PARSING_THEM_BY_ME_FOR_ENJOY == "os":

    t = Teredo('d:\DISC_I\EDIT')

    print('ShowTree: \n\n', t.ShowTree())
    print('ShowFunc: \n\n', t.showfunc)

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

    '''


        # print(t.root.ancestor.root.path)
    # print(t.root.LikeIt())
    # print('SHOW: \n\n', t.root.childs[3].ShowTree())
    # print( "\n".join(["(%d) : %s : %s" % (child.id, child.isnode, child.name) for child in t.root.childs]))

    # print('SHOW-FUNC: \n\n', t.root.ShowFunc())







