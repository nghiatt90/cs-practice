# https://app.codesignal.com/challenge/DBQa6cjuqHt3b6qTx
f, l, g = eval(dir()[0])
return re.findall(f + ' ?(?=([A-Z][a-z]*) ?%s)' % l, g)


