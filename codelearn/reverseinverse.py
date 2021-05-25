# https://codelearn.io/training/detail/43261
def reverseInverse(s):
    words = []
    current = ''
    for c in s:
        if not c.isalnum():
            if current:
                words.append(current)
                current = ''
            words.append(c)
        else:
            current += c
    if current:
        words.append(current)
    
    def reverse_word(word):
        if len(word) == 1 and not word.isalnum():
            return word
        out_rev = []
        for i, c in enumerate(word[::-1]):
            if word[i].isupper() or word[i].isnumeric():
                out_rev.append(c.lower())
            else:
                out_rev.append(c.upper())
        return ''.join(out_rev)

    return ''.join(reverse_word(word) for word in words)
