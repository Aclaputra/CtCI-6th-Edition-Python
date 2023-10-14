import unittest

def is_unique_chars_algorithmic(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    
    return True

def is_unique_bit_vector(string):
    if len(string) > 128:
        return False
    
    checker = 0
    for c in string:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
        
    return True

def is_unique_chars_using_dictionary(string: str) -> bool:
    character_counts = {}
    
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
        
    return True

def is_unieue_chars_algorithmic(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

class TestAlgorithmic(unittest.TestCase):
    def test_is_unique_chars_alphabet(self):
        assert(is_unique_chars_algorithmic("abcd") == True)
        
    def test_is_unique_chars_same(self):
        assert(is_unique_chars_algorithmic("23ds2") == False)
    
class TestAlgorithmic(unittest.TestCase):
    def test_is_unique_chars_alphabet(self):
        assert(is_unique_chars_algorithmic("abcd") == True)
        
    def test_is_unique_chars_same(self):
        assert(is_unique_chars_algorithmic("23ds2") == False)
        
if __name__ == "__main__":
    unittest.main()