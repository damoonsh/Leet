# Given two string, decide if one is a permutation of the other one


# Which one's bigger?
# if the number of letters in smaller one matched (less than or equal) the big one, then it is a match

def CheckPerm(s1: string, s2: string):
    if s1 == s2: return True
    if s1 == "" or s2 == "": return False

    if len(s1) > len(s2):
        big, sml = s1, s2
    else:
        big, sml = s2, s1

    lmap_big, lmap_sml = [0 for i in range(26)], [0 for i in range(26)]

    for i in range(len(big)):
        if i + 1 <= len(sml):
            lmap_sml[ord(sml[i]) - ord('a')] += 1
        
        lmap_big[ord(big[i]) - ord('a')] += 1


    for i in range(26):
        if lmap_big[i] < lmap_sml[i]: return False

    
    return True