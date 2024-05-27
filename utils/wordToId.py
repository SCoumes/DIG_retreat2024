from typing import Optional
import os

def wordToId(word : str) -> Optional[int]:
    """
    @param word: A string representing a word to encode.
    @return: An integer representing the encoding of the word as an ID on the board (including nationalities) or None if it wasn't found.
    """
    with open(os.path.join('utils','codes.csv'), 'rt', encoding='utf-8') as codes:
        for line in codes:
            split=line[:-1].lower().split(',')
            if int(split[0]) == 115 : 
                pass
            for w in split[1:]:
                if word.lower() == w.lower():
                    return int(split[0])
    return None