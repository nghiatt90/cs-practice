# https://codelearn.io/training/detail/34555
def romaji(s):
    is_vowel = lambda x: x in 'aiueo'
    is_consonant = lambda x: not is_vowel(x) and x != 'n'
    for i in range(1, len(s)):
        if is_consonant(s[i-1]) and not is_vowel(s[i]):
            return False
    return not is_consonant(s[-1])
        
