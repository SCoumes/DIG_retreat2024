from typing import List, Optional

class Node:
    
    children : List["Node"]
    comment : str

    def __init__(self, comment = "No comment") -> None:
        self.children = []
        self.comment = comment

    def addChild(self, neighbor : "Node") -> None:
        self.children.append(neighbor)

    def setComment(self, txt):
        self.comment = txt

    def getComment(self): 
        return self.comment
    
    def __str__(self) -> str:
        return self.comment

class RootNode(Node):

    txt : str

    def __init__(self, txt, comment = "No comment") -> None:
        super().__init__(comment)
        self.txt = txt

class LeafNode(Node):

    cellID : int

    def __init__(self, cellID, comment = "No comment") -> None:
        super().__init__(comment)
        self.cellID = cellID

class Graph:
    nodes : List[Node]
    root : RootNode

    def __init__(self, nodes, root) -> None:
        self.nodes = nodes
        self.root = root


# TODO sigs

def getGraph(toEncode  : str) -> Graph:
    pass

def getConceptEncoding(graph : Graph) -> List[List[int]]:
    pass