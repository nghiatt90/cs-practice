// https://app.codesignal.com/challenge/GDQ7MXLtpWKCMXNXy

	int i, l, a[];

	int[] shuffleState(int[] d, int n) {
		a = d.clone();
		l = a.length;
		for (i = 0; i < l; )
			a[i] = d[i / 2 + i++ % 2 * l / 2];
		return n < 1 ? d : shuffleState(a, n - 1);
	}
