
import unittest
import time
from collections import defaultdict


def is_unique(string):
     # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # this is a pythonic and faster way to initialize an array with a fixed value.
    #  careful though it won't work for a doubly nested array
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

def is_unique_v2(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
        
    return True

def is_unique_v3(string):
    if len(string) > 128:
        return False
    
    char_arr = [False] * 128
    for x in string:
        char = ord(x)
        if char_arr[char]:
            return False
        char_arr[char] = True
    
    return True

def is_unique_v4(string):
    if len(string) > 128:
        return False
    
    char_arr = [False] * 128
    for x in string:
        val = ord(x)
        if char_arr[val]:
            return False
        char_arr[val] = True
    
    return True

def is_unique_v5(string):
    if len(string) > 128:
        return False
    
    char_arr = [False] * 128
    for x in string:
        val = ord(x)
        if char_arr[val]:
            return False
        char_arr[val] = True
        
    return True

def is_unique_v6(string):
    if len(string) > 128:
        return False
    
    char_arr = [False] * 128
    for x in string:
        val = ord(x)
        if char_arr[val]:
            return False
        char_arr[val] = True
        
    return True

def is_unique_v7(string):
    if len(string) > 128:
        return False
    
    char_arr = [False] * 128
    for x in string:
        val = ord(x)
        if char_arr[val]:
            return False
        char_arr[val] = True
        
    return True

def is_unique_v8(string):
    if len(string) > 128:
        return False
    
    char_arr = [False] * 128
    for x in string:
        val = ord(x)
        if char_arr[val]:
            return False
        char_arr[val] = True
    
    return True

def is_unique_v9(string):
    characters_counts = {}
    for char in string:
        if char in characters_counts:
            return False
        characters_counts[char] = 1
    
    return True

def is_unique_v10(string):
    if len(string) > 128:
        return False
    
    char_arr = [False] * 128
    for char in string:
        val = ord(char)
        if char_arr[val]:
            return False
        char_arr[val] = True
        
    return True

def is_unique_v11(string):
    if len(string) > 128:
        return False

    char_counts = {}
    
    for x in string:
        if x in char_counts:
            return False
        char_counts[x] = 1
        
    return True

def is_unique_v12(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    for x in string:
        val = ord(x)
        if char_set[val]:
            return False
        char_set[val] = True
        
    return True

def is_unique_v13(string):
    if len(string) > 128:
        return False
    
    char_counts = {}
    for x in string:
        if x in char_counts:
            return False
        char_counts[x] = 1
    
    return True

def is_unique_v14(string):
    if len(string) > 128:
        return False
    
    char_arr = [False] * 128
    for x in string:
        val = ord(x)
        if char_arr[val]:
            return False
        char_arr[val] = True
        
    return True

def is_unique_v15(string):
    if len(string) > 128:
        return False
    
    char_counts = {}
    for x in string:
        if x in char_counts:
            return False
        char_counts[x] = 1
    
    return True

def is_unique_v16(string):
    if len(string) > 128: #3
        return False
    
    char_arr = [False] * 128 
    for x in string: 
        val = ord(x)
        if char_arr[val]: #1
            return False 
        char_arr[val] = True #2
        
    return True

def is_unique_v17(string):
    if len(string) > 128:
        return False

    char_arr = [False] * 128
    for x in string:
        val = ord(x)
        if char_arr[val]:
            return False
        char_arr[val] = True
    
    return True

def is_unique_v18(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    for x in string:
        val = ord(x)
        if char_set[val]:
            return False
        char_set[val] = True
    
    return True

def is_unique_v19(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    for x in string:
        val = ord(x)
        if char_set[val]:
            return False
        char_set[val] = True
    
    return True

def is_unique_v20(string):
    chars_seen = set()
    for char in string:
        if char in chars_seen:
            return False
        chars_seen.add(char)
        
    return True

def is_unique_v21(string):
    if len(string) > 128:
        return False
    
    char_arr = [False] * 128
    for char in string:
        val = ord(char)
        if char_arr[val]:
            return False
        char_arr[val] = True
        
    return True

def is_unique_v22(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    for x in string:
        val = ord(x)
        if char_set[val]:
            return False
        char_set[val] = True
    return True
    
class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique,
        is_unique_v2,
        is_unique_v3,
        is_unique_v4,
        is_unique_v5,
        is_unique_v6,
        is_unique_v7,
        is_unique_v8,
        is_unique_v9,
        is_unique_v10,
        is_unique_v11,
        is_unique_v12,
        is_unique_v13,
        is_unique_v14,
        is_unique_v15,
        is_unique_v16,
        is_unique_v17,
        is_unique_v18,
        is_unique_v19,
        is_unique_v20,
        # is_unique_v21,    
        is_unique_v22,
        # is_unique_chars_pythonic,
        # is_unique_chars_algorithmic,
        # is_unique_bit_vector,
        # is_unique_chars_using_dictionary,
        # is_unique_chars_using_set,
        # is_unique_chars_sorting,
        # is_unique_chars_sort,
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()

