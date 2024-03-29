from core.models import Node, Attribute, Link
from core.services.Visualization import Visualization

class Visualization(Visualization):

    def __init__(self):
        self.name="Visual plugin"
        self.location="visualization"

    def create_dict_nodes(self, nodes):
        tree_child = {}
        for node in nodes:
            children_links = Link.objects.filter(parent_node=node)
            children = []
            for child_link in children_links:
                children.append(child_link.child_node)

            tree_child[node] = self.create_dict_nodes(children)

        return tree_child


    def getTree(self):
        allNodes = Node.objects.all()

        tree = {}
        children_links = Link.objects.filter(parent_node=allNodes[0])
        children = []
        for child_link in children_links:
            children.append(child_link.child_node)
        # print(child_link.child_node)

        tree[allNodes[0]] = self.create_dict_nodes(children)
        return tree



    def addAttributes(self, node, n):
        if node.attrib != {}:
            for key in node.attrib.keys():
                a = Attribute(name=key, value=node.attrib[key])
                a.save()
                n.attributes.add(a)
            n.save()
        return n

    def getSearchTreeById(self, nodeId):
        try:
            node=Node.objects.filter(pk=nodeId)[0]
        except:
            return None
        search_tree = {}
        children_links = Link.objects.filter(parent_node=node)
        children=[]
        for child_link in children_links:
            children.append(child_link.child_node)

        search_tree[node]=self.create_dict_nodes(children)
        return search_tree




