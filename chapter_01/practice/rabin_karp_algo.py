
# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book
 
# d is the number of characters in the input alphabet
d = 256
# total ascii character
 
# pat  -> pattern
# txt  -> text
# q    -> A prime number
 
 
def search(pat, txt, q):
    patternLen = len(pat)
    textLen = len(txt)
    i = 0
    j = 0
    hashPattern = 0    # hash value for pattern
    hashText = 0    # hash value for txt
    h = 1
 
    # The value of h would be "pow(d, M-1)%q"
    for i in range(patternLen-1):
        print(h,d,q)
        h = (h*d) % q
        print(h, "H")
 
    # Calculate the hash value of pattern and first window
    # of text
    for i in range(patternLen):
        hashPattern = (d*hashPattern + ord(pat[i])) % q
        hashText = (d*hashText + ord(txt[i])) % q
        print(hashPattern, "hash pattern")
        print(hashText, "hash text")
 
    # Slide the pattern over text one by one
    for i in range(textLen-patternLen+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters one by one
        if hashPattern == hashText:
            # Check for characters one by one
            for j in range(patternLen):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1
 
            # if hashPattern == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == patternLen:
                print("Pattern found at index " + str(i))
 
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < textLen-patternLen:
            hashText = (d*(hashText-ord(txt[i])*h) + ord(txt[i+patternLen])) % q
 
            # We might get negative values of hashText, converting it to
            # positive
            if hashText < 0:
                hashText = hashText+q
 
 
# Driver Code
if __name__ == '__main__':
    txt = "GEEKS FOR GEEKS"
    pat = "GEEK"
 
    # A prime number
    q = 101
 
    # Function Call
    search(pat, txt, q)
 
# This code is contributed by Bhavya Jain
print(256 % 101)