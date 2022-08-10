from lxml import html as h
from ..models import Node

class LoadHtmlSource:

    def parseHTML(self):
        print("html parser bb")
        html = '<html><body this="asdf"><div class="super" test="super kul"><h1 class="super">Prvi naslov</h1></div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></body></html>'
        tree = h.fromstring(html)

        nodes = tree

        test = []

        saveNode = Node(label=tree.tag)
        saveNode.save()

        while True:
            newNodes = []
            if len(nodes) == 0:

                break
            for node in nodes:
                test.append(node)
                ns = Node(label=node.tag)
                ns.save()

                if node.attrib !={}:
                    for key in node.attrib.keys():
                        print('node text:', node.text, node.tag, '| attributes', key, ':', node.attrib[key] )


                if len(node) > 0:
                    for child in node:
                        newNodes.append(child)
            nodes = newNodes

        for item in test:
            print(item.text, "item", item.attrib)
