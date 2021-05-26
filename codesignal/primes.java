// https://app.codesignal.com/challenge/ub9TmaAnXHHoSSEN5

	int c, i, j;

	int primes(int[] a) {
		for (int x : a)
			c += b(++j) * b(x);
		return c;
	}

	int b(int n) {
		int r = i = 1;
		for (; ++i * i <= n;)
			r = n % i < 1 ? 0 : r;
		return n < 2 ? 0 : r;
	}
