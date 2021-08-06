class A0Paper:
    def canBuild(self, a):
        n = len(a)
        a = list(a)
        for i in xrange(n-1, 0, -1):
            a[i-1] += a[i] >> 1
        return "Possible" if a[0] else "Impossible"
