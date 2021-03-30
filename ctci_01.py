def unique_chars_with_structure(s):
    char_counter = dict()
    for c in s:
        try:
            char_counter[c] += 1

        except KeyError:
            char_counter[c] = 1

    char_set = set(char_counter.values())
    if len(char_set) == 1 and char_set.pop() == 1:
        return True
    
    else:
        return False

def unique_chars_no_structure(s):
    char_detector, mask = 0, 0
    if not s:
        return False

    for c in s:
        mask = 1 << (ord(c) - ord('0'))
        if char_detector & mask:
            return False 
        
        else:
            char_detector |= mask

    else:
        return True

def are_permutation(s1, s2):
    '''Watch for ASCII characters or UNICODE, case sensitive and spaces'''
    if s1 == s2:
        return False
    
    if len(s1) != len(s2):
        return False

    for c in s1:
        if s1.count(c) != s2.count(c):
            return False
    
    else:
        return True 

    
        
    
