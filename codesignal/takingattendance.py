# https://app.codesignal.com/challenge/G5PCB7haet2QXZtGs
return sum(5 + sum(1 << len(g)-1 for g in re.findall('[^aiueoy]+', n, 2)) for n in eval(dir()[0])[0])

