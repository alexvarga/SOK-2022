from lxml import html as h
from core.models import Node, Attribute, Link
import json
from django.core import serializers


class LoadHtmlSource:

    def __init__(self):
        self.name="Html source plugin"
        self.location="source_html"

    def parse(self, filename):

        try:
            Node.objects.all().delete()
        except:
            print("nemam")
        try:
            Attribute.objects.all().delete()
        except:
            print("nothing to delete")

        # html = '<html><body this="asdf"><div class="super" test="super kul"><h1 class="super">Prvi naslov</h1><h2 class="super">drugi naslov</h2></div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></body></html>'
        # tree = h.fromstring(html)
        tree = h.parse('uploads/' + filename)
        root = tree.getroot()

        test = []

        n = Node(label=root.tag, complete=root)
        n.save()

        if root.attrib != {}:
            for key in root.attrib.keys():
                a = Attribute(name=key, value=root.attrib[key])
                a.save()
                n.attributes.add(a)
            n.save()

        if len(root) > 0:

            for child in root:
                linkLabel = root.tag + " + " + child.tag
                link = Link(label=linkLabel)
                link.parent_node = n


                cn = Node(label=child.tag, complete=child)
                if child.text != None and "\n" not in child.text:
                    cn.text=child.text
                    print(child.text)
                else:
                    cn.text=""

                cn.save()
                link.child_node = cn
                link.save()


        nodes = root
        while True:
            newNodes = []
            if len(nodes) == 0:
                break
            for node in nodes:
                test.append(node)
                try:  # is node already saved as someone's child
                    ns = Node.objects.get(complete=node)
                except Node.DoesNotExist:
                    ns = Node(label=node.tag, complete=node, text=node.text)
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
                        if child.text != None and "\n" not in child.text:
                            cn.text = child.text
                            print(child.text)
                        else:
                            cn.text = ""
                        cn.save()
                        link.child_node = cn
                        link.save()
                        newNodes.append(child)
            nodes = newNodes

    def my_to_json(self, all_nodes):
        stringNodes = self.nodeKeys(all_nodes)
        links = {}

        for node in stringNodes:
            links[node] = []
            n = Link.objects.filter(parent_node=Node.objects.filter(pk=node)[0])
            for i in n:
                print(node, " : ", i.child_node.pk)
                links[node].append(str(i.child_node.pk))

        links2 = links

        for key in links:
            for key2 in links:
                if len(links[key]) > 0:
                    if key in links[key2]:
                        print("hello", links[key2])
                        links2[key2].append(links[key])

        links3 = links.copy()

        for key in links:
            for k in links:
                if key in links[k]:
                    links3.pop(key)

        for key in enumerate(links3):
            print(key)

        return json.dumps(links3)

