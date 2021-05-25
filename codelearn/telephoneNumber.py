def telephoneNumber(s):
    """https://codelearn.io/training/detail/34404"""
    return 'YES' if s.find('8') >= 0 and len(s) - s.find('8') >= 11 else 'NO'
