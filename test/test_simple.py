def test_encoderSimple():
    from example import graph
    from getEncoding import getConceptEncoding
    encoding = getConceptEncoding(graph)
    assert(len(encoding) == 2)
    assert(len(encoding[1]) == 2)
    assert(encoding[0][0] == 16)