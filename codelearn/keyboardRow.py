def keyboardRow(words):
    """https://codelearn.io/training/detail/21439"""
    R = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
    res = []
    for word in words:
        S = set(word.lower())
        if any(len(S - r) == 0 for r in R):
            res.append(word)
    return res
