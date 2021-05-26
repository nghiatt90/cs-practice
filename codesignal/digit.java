// https://app.codesignal.com/challenge/DRA8Dy2up5XoHaj6B

	int f[] = new int[10], t, p, k;

	int digit(int L, int R) {
		for (; L <= R;)
			for (t = L++; t > 0; p = ++f[k] > f[p] | f[k] == f[p] & k < p ? k : p, t /= 10)
				k = t % 10;
		return p;
	}

