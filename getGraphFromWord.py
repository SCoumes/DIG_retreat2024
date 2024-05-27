from dataExchange import Graph
from encoding_yago import get_graph

def getGraphFromWord(word : str) -> Graph:
    """
    @param word: A string representing a word to encode.
    @return: A graph representing the local concept-space of the word.
    """
    # from test.example import graph
    return get_graph(word)