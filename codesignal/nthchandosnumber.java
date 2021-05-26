// https://app.codesignal.com/challenge/GdDabcKaafJqYABLi
int nthChandosNumber(int N) {
		int r = 0, i = 1;
		while (N > 0) {
			if (N % 2 > 0) r += Math.pow(5, i);
			++i;
			N /= 2;
		}
		return r;
	}

