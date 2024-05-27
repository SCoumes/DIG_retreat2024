def encode(concept):
    """Encoder for Concept.
    
    Parameter
    ---------
    concept: str
        Concept to encode.
        
    Returns
    -------
    code: list of lists of integers
        Each list corresponds to a marker, starting with the green.
        The first element of each list is the concept (= question or exclamation marker), the others are the attributes (= cubes).
        There are at most 5 lists, each of length at most 10.
        
    Example
    -------
    Concept = Honey
    Code = [[26], [6, 21, 110, 112]]
    Meaning = Food (main concept) related to bees (secondary concept) coded as yellow-and-black flying animals.
    """
    code = [[0]]
    return code
