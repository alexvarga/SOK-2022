from lxml import html as h
from ..models import Node, Attribute, Link


class LoadHtmlSource:

    def parseHTML(self):
        html = '<html><body this="asdf"><div class="super" test="super kul"><h1 class="super">Prvi naslov</h1><h2 class="super">drugi naslov</h2></div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></body></html>'
        tree = h.fromstring(html)

        nodes = tree

        test = []

        saveNode = Node(label=tree.tag, complete=tree)
        saveNode.save()

        while True:
            newNodes = []
            if len(nodes) == 0:
                break
            for node in nodes:
                test.append(node)

                try:  # is node already saved as someone's child
                    ns = Node.objects.get(complete=node)
                except Node.DoesNotExist:
                    ns = Node(label=node.tag, complete=node)
                    ns.save()

                if node.attrib != {}:
                    for key in node.attrib.keys():
                        att = Attribute(name=key, value=node.attrib[key])
                        att.save()
                        ns.attributes.add(att)
                    ns.save()

                if len(node) > 0:
                    for child in node:
                        linkLabel = node.tag + " + " + child.tag
                        link = Link(label=linkLabel)
                        link.parent_node = ns

                        cn = Node(label=child.tag, complete=child)

                        cn.save()

                        link.child_node = cn

                        link.save()

                        newNodes.append(child)
            nodes = newNodes
