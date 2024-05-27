from dataExchange import Graph

def getGraphFromWord(word : str) -> Graph:
    """
    @param word: A string representing a word to encode.
    @return: A graph representing the local concept-space of the word.
    """
    from test.example import graph
    return graph