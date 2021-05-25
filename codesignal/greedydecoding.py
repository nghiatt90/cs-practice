# https://app.codesignal.com/challenge/JhtBKjkeDwaaERovM
greedyDecoding = lambda m: ''.join(chr(int(t)+64) for t in re.findall('1.|2[0-6]|0*[1-9]', m))
