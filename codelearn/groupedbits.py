# https://codelearn.io/training/detail/40509
import re

groupedBits = lambda n: len(re.findall('1+', bin(n)))
