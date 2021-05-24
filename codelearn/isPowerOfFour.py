# https://codelearn.io/training/detail/18003
import re

isPowerOfFour = lambda n: bool(re.match('^0b1(00)*$', bin(n)))
