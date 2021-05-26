// https://app.codesignal.com/challenge/gqdK6vmBLGdhyrg2L

	int f[] = new int[999], n, m, k;

	int yTimes(int[] A) {
		k = A[0];
		for (int i : A)
			f[i]++;
		for (int i : A)
			if (i != k & f[i] != f[k])
				if (n < 1) n = i;
				else if (i != n) m = i;
		return n < 1 ? -1 : m < 1 | f[m] == f[k] ? n : k;
	}
