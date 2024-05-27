from typing import List
from dataExchange import Graph, Node, RootNode, LeafNode

nationalities = {
    1000 : [110, 112]
}

def getConceptEncoding(graph : Graph):
    root = graph.root
    result = []
    
    # Main concept and nationalities
    result.append(getMainAndCubes(root))
    for node in root.children:
        if isinstance(node, LeafNode): 
            if node.cellID not in nationalities.keys(): continue
            result.append(nationalities[node.cellID])

    # Other subconcepts
    otherResults = []
    for node in root.children:
        if isinstance(node, LeafNode): continue
        otherResults.append(getMainAndCubes(node))
    otherResults.sort(key = lambda list : -len(list))

    return result + otherResults

def getMainAndCubes(mainNode : Node) -> List[int]:
    greenCubes : List[int] = [node.cellID for node in mainNode.children if isinstance(node, LeafNode)]
    greenCubes.sort()
    return greenCubes[:9]

