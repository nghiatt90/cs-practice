# https://app.codesignal.com/challenge/XeoQpGeAjTzTbHgfu

	int j, b, c;

	int sumofprimenumbers(int t, int[] a) {
		for (int i : a) {
			for (b = j = 1; ++j * j <= i;)
				b *= i % j;
			t = b > 0 & i > 1 ? i : 0;
			for (; t > 0; t /= 10)
				c += t % 10;
		}
		return c;
	}
