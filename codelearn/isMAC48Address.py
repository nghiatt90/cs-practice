import re

def isMAC48Address(x):
    """https://codelearn.io/training/detail/3895"""
    return re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", x.lower()) is not None
