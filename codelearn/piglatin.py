# https://codelearn.io/training/detail/34808
def piglatin(word):
    if word[0] in 'aiueoy':
        return word + 'way'
    word = list(word)
    for i in range(len(word)):
        if word[i] in 'aiueoy':
            break
        word.append(word[i])
    return ''.join(word[i:]) + 'ay'
