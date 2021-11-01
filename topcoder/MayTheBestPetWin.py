# https://community.topcoder.com/stat?c=problem_statement&pm=12779

class MayTheBestPetWin:
	def calc(self, a, b):
		c = [x+y for x, y in zip(a, b)]
		total = [0]*(10000*2*len(a)+1)
		total[0] = 1
		current = 0
		for i, x in enumerate(c):
			for j in xrange(current+1, -1, -1):
				if total[j]:
					total[j+x] = 1
			current += x

		ans = int(1e9)
		for i in xrange(current+1):
			if total[i]:
				m = max(i, current-i)
				ans = min(m, ans)
		return ans - sum(a)
