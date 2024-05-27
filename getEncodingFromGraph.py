from typing import List
from dataExchange import Graph, Node, RootNode, LeafNode
from utils import natioToConcept

def getConceptEncoding(graph : Graph):
    root = graph.root
    result = []
    
    # Main concept and natioToConcept
    result.append(getMainAndCubes(root))
    for node in root.children:
        if isinstance(node, LeafNode): 
            if node.cellID not in natioToConcept.keys(): continue
            result.append(natioToConcept[node.cellID])

    # Other subconcepts
    otherResults = []
    for node in root.children:
        if isinstance(node, LeafNode): continue
        otherResults.append(getMainAndCubes(node))
    otherResults.sort(key = lambda list : -len(list))

    return result + otherResults

def getMainAndCubes(mainNode : Node) -> List[int]:
    """
    Return the "green cubes" from the game Concept.
    @param mainNode: The main node of the graph.
    @return: A list of integers representing the question mark and green cubes of the main concept.
    """
    greenCubes : List[int] = [node.cellID for node in mainNode.children if isinstance(node, LeafNode) and node.cellID not in natioToConcept.keys()]
    greenCubes.sort()
    return greenCubes[:9]

