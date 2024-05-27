from dataExchange import Node, RootNode, LeafNode, Graph

root = RootNode("Pompei")
l1 = LeafNode(16)
l1.setComment("Location")
root.addChild(l1)
l2 = LeafNode(37)
l2.setComment("Death")
root.addChild(l2)
l3 = LeafNode(1024)
l3.setComment("Italy")
root.addChild(l3)
nodes = [root, l1, l2, l3]
graph = Graph(nodes, root)