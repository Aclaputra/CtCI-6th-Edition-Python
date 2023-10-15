
# mirip two sum
def solve(string, to_find) -> bool:
    isTrue = {}
    for x in string:
        for y in to_find:
            if x == y:
                isTrue[y] = True
                continue
            
            if y in isTrue:
                continue
        
            isTrue[y] = False
        
    for y in isTrue:
        if isTrue[y] == False:
            return False
                  
    return True

def solve_v2(string, to_find) -> bool:
    isTrue = [False] * len(to_find)
    for x in range(len(string)):
        valStr = string[x]
        for y in range(len(to_find)):
            print(y, "Y", to_find[y])
            valToFind = to_find[y]
            if valToFind == valStr:
                isTrue[y] = True # get the first same
                   
    print(isTrue)
        
    return True

def solve_v3(string, to_find) -> bool:
    chars_seen = set()
    chars_seen.add("hello")
    chars_seen.add("hello")
    print(chars_seen.difference())
    
    return True
    
# print(solve("ikan", "an"))
# print(solve("ikan", "ian"))
# print(solve("ikan", "o"))

print(solve_v3("ikan", "an"))
print(solve_v3("ikan", "ian"))
print(solve_v3("ikan", "o"))