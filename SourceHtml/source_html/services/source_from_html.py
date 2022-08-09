from lxml import etree



class LoadHtmlSource:

    def parseHTML(self):
        print("html parser bb")
        html = "<html><body><div><h1>Prvi naslov</h1></div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></body></html>"
        root = etree.fromstring(html)

        nodes = root

        test=[]


        while True:
            newNodes=[]
            if len(nodes) == 0:
                print('stigli smo do 0')
                break
            for node in nodes:
                print(node)
                test.append(node)

                if len(node)>0:
                    for child in node:
                        newNodes.append(child)
            nodes=newNodes

        for item in test:
            print(item.text, "item")