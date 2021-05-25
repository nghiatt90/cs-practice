# https://codelearn.io/training/detail/34548
def playfulVowel(s):
    s = s.lower()
    def is_vowel(c):
        return c in 'aiueo'
    def is_consonant(c):
        return c.isalpha() and not is_vowel(c)
    vowels = 'aiueo'
    return sum(is_vowel(s[i]) and is_consonant(s[i-1]) and is_consonant(s[i+1]) for i in range(1, len(s)-1))
