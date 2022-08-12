from lxml import html as h
from ..models import Node, Attribute, Link
import json
from django.core import serializers


class LoadHtmlSource:

    def parse(self, filename):

        Node.objects.all().delete()
        Attribute.objects.all().delete()

        # html = '<html><body this="asdf"><div class="super" test="super kul"><h1 class="super">Prvi naslov</h1><h2 class="super">drugi naslov</h2></div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></body></html>'
        # tree = h.fromstring(html)
        tree = h.parse('uploads/' + filename)
        root = tree.getroot()
        nodes = root
        test = []

        saveNode = Node(label=root.tag, complete=root)
        saveNode.save()
        # child here missing
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

    def create_dict_nodes(self, nodes):
        tree_child = {}
        for node in nodes:
            children_links = Link.objects.filter(parent_node=node)
            children = []
            for child_link in children_links:
                children.append(child_link.child_node)
            # print(child_link.child_node)
            # print(child_link.child_node.id)

            tree_child[node] = self.create_dict_nodes(children)

        return tree_child



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

        links3=links.copy()


        for key in links:
            for k in links:
                if key in links[k]:
                    links3.pop(key)





        for key in enumerate(links3):
            print(key)




        return json.dumps(links3)

    def getTree(self):
        root = Node.objects.all()
        print("root ", root[0])
        tree = {}
        children_links = Link.objects.filter(parent_node=root[0])
        children = []
        for child_link in children_links:
            children.append(child_link.child_node)
        # print(child_link.child_node)

        tree[root[0]] = self.create_dict_nodes(children)
        return tree




    def nodeKeys(self, nodes):
        result = []
        for node in nodes:
            result.append(str(node.id))
        return result