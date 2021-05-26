# https://app.codesignal.com/challenge/LSDiZwGRgCHHao9WN
def f(r, i, v, a):
	if i < 0 or i >= len(a) or a[i] == 0:
		return r
	if v[i] == 1:
		return -1
	v[i] = 1
	if a[i] % 2 == 1:
		r = r + min(a[i], i)
		i = i - a[i]
	else:
		r = r + min(a[i], len(a) - i - 1)
		i = i + a[i]
	return f(r, i, v, a)
def danceSteps(s):
	a = list(map(int, s))
	v = [0] * len(s)
	return f(0, 0, v, a)
