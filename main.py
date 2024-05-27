from typing import List

from utils import hardcodedConcepts
from getGraphFromWord import getGraphFromWord
from getEncodingFromGraph import getConceptEncoding

def encodeConcept(toEncode : str) -> List[List[int]]:
    """
    @param toEncode: A string representing a concept among the 500 hundreds to encode.
    @return: A list of lists of integers representing the encoding of the concept.
    """
    toEncode = toEncode.lower()
    if toEncode in hardcodedConcepts.keys():
        return hardcodedConcepts[toEncode]
    return getConceptEncoding(getGraphFromWord(toEncode))

if __name__ == "__main__":
    toEncode = input("Enter the concept to encode: ")
    print(encodeConcept(toEncode))