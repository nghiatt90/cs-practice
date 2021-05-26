# https://app.codesignal.com/challenge/fRE4enG7w5fgZAcEy
# extraCreditAssignment = lambda s, d: int(float(re.sub("\((.+)\)", r"\1"*9, s))*d+.9)
s, d = eval(dir()[0])
return int(float(re.sub("\((.+)\)", r"\1"*9, s))*d+.9)
