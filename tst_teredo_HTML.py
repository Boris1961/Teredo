# coding=utf-8

from teredo import *

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

t = Teredo(html_doc, 'html')

print(t)

#print(t.root.get_pattern())
#print('ShowTree: \n\n', t.showtree)
#print('ShowFunc: \n\n', t.down.showfunc)

li = t.root.get_pattern_all().items()
li = sorted([(k.name, v) for (k,v) in li])
print(li)
#for (k,v) in li:
#    print(k.name, '  ---->  ', v, '\n')


# print(t.down.get_pattern(wrapper_body=lambda x: "%s(%s)" % (x.name, len(x.tag.attrs))))

# print('SHOW: \n\n', t.ShowTree(lambda x: "\t"*x.floor + "%s(%s)\n" % (x.name, len(x.tag.attrs))))


# print('SHOW: \n\n', t.ShowTree(lambda x: "\t" * x.floor + "%s(%s)\n" % (x.name, len(x.tag.attrs))))
# print('ShowFunc: \n\n', t.down)
# print('SHOW: \n\n', t.down.down.ShowTree(lambda x: "\t" * x.floor + "%s(%s)\n" % (x.name, len(x.tag.attrs))))
# print('=====',t.tree.elements[13].childs[1])
# print('=====',t.tree.elements[13].childs[1].LikeIt()[0])
# print('=====',t.tree.elements[13].childs[1].LikeIt()[1])
# print(t.tree.elements[10].LikeIt()[0].tag)
# print('SHOW: \n\n', t.ShowTree(lambda x: "\t" * x.floor + "%s(%s)\n" % (x.name, ','.join(list(x.tag.attrs.keys())))))
