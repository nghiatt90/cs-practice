# https://codelearn.io/training/detail/6188
coolString = lambda s: all(s[i-1].islower() != s[i].islower() for i in range(1, len(s)))

