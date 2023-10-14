
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

    
print(solve("ikan", "an"))
print(solve("ikan", "ian"))
print(solve("ikan", "o"))