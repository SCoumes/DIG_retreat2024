def test_encoderSimple():
    from test.example import graph
    from getEncodingFromGraph import getConceptEncoding
    encoding = getConceptEncoding(graph)
    assert(len(encoding) == 2)
    assert(len(encoding[1]) == 3)
    assert(encoding[0][0] == 16)

def test_wordToInt():
    from utils import wordToId
    assert(wordToId("Purple") == 115)

def test_encodeHardcoded():
    from main import encodeConcept
    assert(encodeConcept("Virus") == [[47, 97, 97, 97], [], [], [], []])

def test_mainDoesntCrash():
    from main import encodeConcept
    encodeConcept("Brad Pitt")